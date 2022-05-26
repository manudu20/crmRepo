import psycopg2
import pandas as pd
import csv

try:
    connection = psycopg2.connect(user="cms",
                                  password="cms123",
                                  host="172.18.0.4",
                                  port="5432",
                                  database="admin")
    cursor = connection.cursor()
    sql = "select id,author,published_on,blog_text,created_on,created_month from cms.cms_view"

    df = pd.read_sql_query(sql,connection)

    for index,row in df.iterrows():
        filename1 = row['author'] + '-' + str(row['created_month']) + '-' + 'Published-blogs' + '.csv'
        filename2 = row['author'] + '-' + str(row['created_month']) + '-' + 'Draft-blogs' + '.csv'

        file1 = open(str(filename1),'w')
        w = csv.writer('/result/' + file1)
        w.writerow([row['id'],row['author'],row['published_on'],row['blog_text'],row['created_on']])
        file1.close()

        file2 = open('/result/' + str(filename2),'w')
        w = csv.writer(file2)
        w.writerow([row['id'],row['author'],row['published_on'],row['blog_text'],row['created_on']])
        file2.close()

except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)

finally:
        # closing database connection.
        if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")

