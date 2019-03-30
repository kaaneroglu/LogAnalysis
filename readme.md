# Logs Analysis

This is a reporting tool that prints out three reports based on the data in the database. It is a Python program using the psycopg2 module to connect to the "news" database.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Prerequisites

You will need a system that has PostgreSQL and Python3 installed to be able to run this code. This project assumes you have these already setup. If you don't, please find instructions on Google based on your system (Windows/MacOS/Unix).


### Installing

You can install psql and python on your system or use a VM that already has these installed.

Download the project from github and create a folder named "LogAnalysis" and unzip the files.
Next, download the data [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip). You will need to unzip this file after downloading it. The file inside is called newsdata.sql. Put this file into the "LogAnalysis" folder you just created.

To load the data, cd into the vagrant directory and use the command 
```
psql -d news -f newsdata.sql
```

Here's what this command does:
```
psql — the PostgreSQL command line program

-d news — connect to the database named news which has been set up for you

-f newsdata.sql — run the SQL statements in the file newsdata.sql
```

Running this command will connect to your installed database server and execute the SQL commands in the downloaded file, creating tables and populating them with data. After this is completed go into the "LogAnalysis" folder on your console and type the command below to run the report;
```
python log.py
```

## Authors

* **Kaan Eroglu** - *Initial work* - [kaan.ca](https://www.kaan.ca)
* **Udacity FSND Instructions** - *Installation instructions*


## License

This project is licensed under the MIT License 

## Acknowledgments

* Udacity mentors
* Double shot americanos
