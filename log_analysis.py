#!/usr/bin/env python3
import psycopg2
import sys
from termcolor import cprint

db = psycopg2.connect("dbname=news")
cursor = db.cursor()

def get_quiry(quiry):
    cursor.execute(quiry)
    q = cursor.fetchall()
    return q

def result(question,quiry,formating):
    cprint(question,
           'red', attrs=['bold'], file=sys.stderr)
    for result in quiry:
        print(formating.format(result[0], result[1]))

result('What are the most popular three articles of all time?',get_quiry(
    '''
    select articles.title, count(log.path) as views from articles, log
    where log.path = concat('/article/',slug)
    group by articles.title
    order by views desc limit 3;
    '''
     ), '* "{0}" -- {1} views')

result('Who are the most popular article authors of all time?',get_quiry(
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
     ), '* "{0}" -- {1} views')

result('Who are the most popular article authors of all time?',get_quiry(
    '''
    select Date(time) as date ,round(100.0* sum(CASE
    WHEN status = '404 NOT FOUND' THEN 1 ELSE 0 END)/count(status),2) as error
    from log
    group by date
    having round(100.0* sum(CASE WHEN status = '404 NOT FOUND' THEN 1 ELSE 0 END)/count(status),2) > 1
    order by error desc
    '''
     ), '* {0:%b %d, %Y} -- {1}% error')

db.close()
