# "Database code" for the DB Forum.

import psycopg2
import sys

# Database connection for PostgreSQL
db = psycopg2.connect("dbname=news")

# Queries for functions (popular article query, popular author query, day error query)
pop_artcl_qry= "SELECT articles.title, views.view_count " \
               "FROM articles, " \
                "(SELECT SUBSTRING (path, 10) AS article_title, count(id) AS view_count FROM log WHERE path like '/article/%' group by article_title) AS views " \
               "WHERE articles.slug LIKE views.article_title " \
               "ORDER BY views.view_count desc LIMIT 3"

pop_auth_qry= "SELECT authors.name, sum(views.view_count) as author_views " \
              "FROM articles, (SELECT SUBSTRING (path, 10) AS article_title, count(id) AS view_count FROM log WHERE path like '/article/%' group by article_title) AS views, authors " \
              "WHERE articles.slug LIKE views.article_title AND authors.id = articles.author " \
              "GROUP BY authors.name " \
              "ORDER BY author_views desc;"

day_error_qry= "SELECT * " \
              "FROM " \
              "(SELECT error_table.error_days, ROUND(((error_table.error_count*100.0)/total_table.view_count),2) as error_perc " \
                "FROM (SELECT count(id) as view_count, to_char(date_trunc('day', time), 'YYYY-MM-DD') as view_days FROM log GROUP BY view_days) total_table " \
              "LEFT JOIN " \
              "(SELECT count(id) as error_count, to_char(date_trunc('day', time), 'YYYY-MM-DD') as error_days " \
                "FROM log WHERE status like '404 NOT FOUND' GROUP BY error_days) error_table " \
              "ON (total_table.view_days = error_table.error_days)) results " \
              "WHERE error_perc>1"


def pop_artcl():
    """Return articles have been accessed the most (Top 3)."""
    cur = db.cursor()
    cur.execute(pop_artcl_qry)
    return cur.fetchall()
    cur.close()
    db.close()


def pop_auth():
    """Return author names got the most page views."""
    cur = db.cursor()
    cur.execute(pop_auth_qry)
    return cur.fetchall()
    cur.close()
    db.close()


def day_error():
    """Return days which got more than 1% of requests lead to errors."""
    cur = db.cursor()
    cur.execute(day_error_qry)
    return cur.fetchall()
    cur.close()
    db.close()


print('')
print('Most Popular Articles')
print('---------------------')
for x, y in pop_artcl():
    print('"{0}" -- {1} views'
          .format(x, y))
print('')
print('Most Popular Authors')
print('--------------------')
for x, y in pop_auth():
    print('{0} -- {1} views'
          .format(x, y))
print('')
print('Days with error rate higher than 1%')
print('-----------------------------------')
for x, y in day_error():
    # print integer and float value
    print('{0} -- {1:2f}%'
          .format(x, y))
