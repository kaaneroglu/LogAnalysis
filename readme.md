# Logs Analysis

This project sets up a mock PostgreSQL database for a fictional news website. The provided Python script uses the psycopg2 library to query the database and produce a report that answers the following three questions:
* What are the most popular three articles of all time?
* Who are the most popular article authors of all time?
* On which days did more than 1% of requests lead to errors?
## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Prerequisites

You will need a system that has PostgreSQL and Python3 installed to be able to run this code. This project assumes you have these already installed, along with a blank "news" database to populate the mock dataset. If you don't, please find instructions on Google based on your system (Windows/MacOS/Unix).


### Installing

You can install psql and python on your system or use a VM that already has these installed. (Recommended to use Vagrant as VM, you can use [this Vagrantfile](https://github.com/udacity/fullstack-nanodegree-vm/blob/master/vagrant/Vagrantfile) provided by Udacity to set up your virtual machine with a blank news database)

Download the project from github and create a folder named "LogAnalysis" and unzip the files.
Next, download the data for news database [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip). You will need to unzip this file after downloading it. The file inside is called newsdata.sql. Put this file into the "LogAnalysis" folder you just created.

To load the data, cd into the vagrant directory and use the command below (Make sure you have a blank news database if you didn't use the Vagrantfile above)
```
psql -d news -f newsdata.sql
```

Here's what this command does:
```
psql — the PostgreSQL command line program

-d news — connect to the database named news (created by the vagrantfile, or by you if you are not using a VM)

-f newsdata.sql — run the SQL statements in the file newsdata.sql
```

Running this command will connect to your installed database server and execute the SQL commands in the downloaded file, creating tables and populating them with data. After this is completed go into the "LogAnalysis" folder on your console and type the command below to run the report;
```
python3 logs.py
```

## References / Authors

* **Kaan Eroglu** - *Initial work* - [kaan.ca](https://www.kaan.ca)
* **Udacity FSND Instructions** - *Installation instructions*


## License

This project is licensed under the MIT License 

## Acknowledgments

* Udacity mentors
* Double shot americanos
