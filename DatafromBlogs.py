import psycopg2
import csv
try:
    connection = psycopg2.connect(user="cms",
                                  password="cms123",
                                  host="172.18.0.4",
                                  port="5432",
                                  database="admin")
    cursor = connection.cursor()
    sql = "select id,author,published_on,blog_text,created_on,created_month from cms.cms_view"

    cursor.execute(sql)
    data = cursor.fetchall()
    for row in data:
        basefilename = row[1] + '-' + str(row[5])
        file = open('/result/' + str(basefilename) + '-' + 'Published-blogs' + '.csv' ,'w')
        w = csv.writer(file)
        w.writerow([row[0],row[1],row[2],row[3],row[4]])
        file.close()

        file1 = open('/result/' + str(basefilename) + '-' + 'Draft-blogs' + '.csv' ,'w')
        w = csv.writer(file1)
        w.writerow([row[0],row[1],row[2],row[3],row[4]])
        file1.close()

except (Exception, psycopg2.Error) as error:
    print("Error while fetching data from PostgreSQL", error)

finally:
    # closing database connection.
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
