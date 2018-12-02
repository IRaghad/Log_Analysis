# Log_Analysis
It is reporting tool to analyze tho logs of newspaper .
it use information from the database to discover what kind of articles the site's readers like.

# Get Started 
Follow the instructions to run the reporting tool!

- first you need to dowload and install :
1. [Virtual Box](https://www.virtualbox.org/wiki/Downloads)
2. [Vagrant ](https://www.vagrantup.com/downloads.html)


- second downlooad the the Vagrantfile : 

[Vagrantfile](https://github.com/udacity/fullstack-nanodegree-vm)


- Once you get the above software installed, follow the following instructions:
```
$cd vagrant
$vagrant up
$vagrant ssh
```

- Then you need to download the database file and unzip the file inside Vagrant folder : 

[Database](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)

- run these commands: 

```
$pip3 install psycopg2
$pip3 install pycodestyle
$pip3 install termcolor
```
- Import the database using this command : 
```
$psql -d news -f newsdata.sql 
```
# Run the file
run the file using this command : 
```
$python3 log.py 
```
output :
<br>
<img height=170 src=https://github.com/IRaghad/Log_Analysis/blob/master/Screen%20Shot%20of%20the%20output.png />
