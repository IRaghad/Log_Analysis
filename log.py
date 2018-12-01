import psycopg2

db = psycopg2.connect("dbname=news")
cursor = db.cursor()
cursor.execute(
    '''
    select articles.title, count(log.path) as views from articles, log
    where log.path = concat('/article/',slug)
    group by articles.title
    order by views desc limit 3;
     '''
)
one = cursor.fetchall()
cursor.execute(
    '''
    select authors.name, count(log.path) as views from articles, log, authors
    where log.path = concat('/article/',slug)
    And
    Authors.id = articles.author
    group by
    authors.name
    order by
    views desc;
    '''
)
two = cursor.fetchall()
cursor.execute(
    '''
    select Date(time) as date ,round(100.0* sum(CASE WHEN status = '404 NOT FOUND' THEN 1 ELSE 0 END)/count(status),2) as error
    from log
    group by date
    order by error desc;
    '''
)
three = cursor.fetchall()

a = '* "{0}" -- {1} views'
b = '* {0:%b %d, %Y} -- {1}% error'
print('What are the most popular three articles of all time?')
for result in one:
    print(a.format(result[0], result[1]))
print('Who are the most popular article authors of all time?')
for result in two:
    print(a.format(result[0], result[1]))
print('On which days did more than 1% of requests lead to errors?')

for result in three:
    if result[1] > 1:
        print(b.format(result[0], result[1]))
db.close()
