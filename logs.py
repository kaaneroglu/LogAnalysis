#!/usr/bin/env python3

"""This code was created as a project submission to Udacity's Full Stack Web Developer Nanodegree program.
It demonstrates ability to connect to a PostgreSQL database and run different SELECT queries based on 3 questions,
then displays the results in a formatted/readable way. Please check the README file for instructions to run the code."""

import psycopg2

# Query for "What are the most popular three articles of all time?"
pop_artcl_qry = """SELECT articles.title, views.view_count
              FROM articles,
              (SELECT SUBSTRING (path, 10) AS article_title, count(id) AS view_count FROM log WHERE path like '/article/%' group by article_title) AS views
              WHERE articles.slug LIKE views.article_title
              ORDER BY views.view_count desc LIMIT 3"""

# Query for "Who are the most popular article authors of all time?"
pop_auth_qry = """SELECT authors.name, sum(views.view_count) as author_views
              FROM articles,
              (SELECT SUBSTRING (path, 10) AS article_title, count(id) AS view_count FROM log WHERE path like '/article/%' group by article_title) AS views,
              authors
              WHERE articles.slug LIKE views.article_title
              AND authors.id = articles.author
              GROUP BY authors.name
              ORDER BY author_views desc"""

# Query for "On which days did more than 1% of requests lead to errors?"
day_error_qry = """SELECT *
              FROM
              (SELECT error_table.error_days, ROUND(((error_table.error_count*100.0)/total_table.view_count),2) as error_perc
              FROM (SELECT count(id) as view_count, time::date as view_days FROM log GROUP BY view_days) total_table
              LEFT JOIN
              (SELECT count(id) as error_count, time::date as error_days FROM log WHERE status like '404 NOT FOUND' GROUP BY error_days) error_table
              ON (total_table.view_days = error_table.error_days)) results
              WHERE error_perc>1"""


# Function to run quertes on the Database, it takes the query as input and returns results
def db_execute(query):
    db = psycopg2.connect("dbname=news")
    cur = db.cursor()
    cur.execute(query)
    results = cur.fetchall()
    cur.close()
    db.close()
    return results


# Function to generate the report when the code is executed directly
def main():
    """Generate Report."""
    print('')
    print('Most Popular Articles')
    print('---------------------')
    for x, y in db_execute(pop_artcl_qry):
        print('"{0}" -- {1} views'
              .format(x, y))
    print('')
    print('Most Popular Authors')
    print('--------------------')
    for x, y in db_execute(pop_auth_qry):
        print('{0} -- {1} views'
              .format(x, y))
    print('')
    print('Days with error rate higher than 1%')
    print('-----------------------------------')
    for x, y in db_execute(day_error_qry):
        print('{0} -- {1:2f}%'
              .format(x, y))


# Condition to check whether the code is executed directly to call the main subroutine
# This program can be imported as a module to utilize the db_execute function.
if __name__ == '__main__':
    main()
