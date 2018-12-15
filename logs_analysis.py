#!/usr/bin/env python3
# 
# A program to answer Udacity FSND Project - Logs Analysis questions.

import psycopg2

# Database queries
# Database query 1: What are the three most popular articles of all time?
articles_query = """SELECT articles.title, count(log.id) AS Views 
                      FROM log, articles 
                      WHERE log.status = '200 OK' 
                      AND log.path LIKE '%article%' 
                      GROUP BY log.path, articles.title, articles.slug HAVING substring(log.path,10) = articles.slug 
                      ORDER BY Views DESC LIMIT 3;"""

# Database query 2: Who are the most popular article authors of all time?
authors_query = """SELECT name, count(*) as Views 
                     FROM authors, articles, log 
                     WHERE log.status = '200 OK' 
                     AND substring(log.path,10) = articles.slug 
                     AND authors.id = articles.author 
                     GROUP BY authors.name
                     ORDER BY Views desc; """

# Database query 3: On which day did more than 1% of requests lead to errors?
log_query = """ SELECT day, ratio 
                FROM (
                    SELECT day, (cast(badReq as decimal)/cast(totalReq as decimal)*100.00) AS ratio 
                    FROM (
                        SELECT to_char(time, 'Mon dd,yyyy') AS day, count(CASE WHEN status != '200 OK' THEN 1 END) AS badReq, count(*) as totalReq 
                        FROM log GROUP BY day ORDER BY day
                        ) as fail_logs
                    ) as final_fail_logs 
                WHERE ratio > 1.0; """

#Execute query and return all rows
def db_query(query):
    db = psycopg2.connect(database="news")
    cursor = db.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    db.close()
    return results

#Print the most popular three articles of all time
def top_three_articles():
    print ("Top 3 Articles:\n")
    top_three_articles = db_query(articles_query)

    for title, views in top_three_articles:
        print(" \"{}\" -- {} views".format(title,views))

#Print the most popular article authors of all time
def top_authors():
    print ("\nTop Authors:\n")
    top_authors = db_query(authors_query)

    for author, views in top_authors:
        print(" {} -- {} views".format(author,views))

#Print the days where failure rate is more than 1%
def fail_logs():
    print ("\nDays with over 1% failure rate:\n")
    failures = db_query(log_query)

    for day, rate in failures:
        print(" {0} -- {1:.2f} % errors".format(day,rate))

if __name__ == '__main__':
    top_three_articles()
    top_authors()
    fail_logs()






