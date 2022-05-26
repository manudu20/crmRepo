import psycopg2
import csv
import configparser

#Initilize config session
config = configparser.ConfigParser()
try:
    config.read('config.ini')
except Exception as e:
    print('can not read config.ini file '+str(e))
    sys.exit()

#read config files
postgreDBUser = config['POSTGREDBCONFIG']['postgreDBUser']
postgreDBpwd = config['POSTGREDBCONFIG']['postgreDBpwd']
postgreDBhostIP = config['POSTGREDBCONFIG']['postgreDBhostIP']
postgreDBport = config['POSTGREDBCONFIG']['postgreDBport']
postgreDBDB = config['POSTGREDBCONFIG']['postgreDBDB']
sqlQuery  = config['POSTGREDBCONFIG']['sqlQuery']

#connect to postgresql DB
try:
    connection = psycopg2.connect(user=postgreDBUser,
                                  password=postgreDBpwd,
                                  host=postgreDBhostIP,
                                  port=postgreDBport,
                                  database=postgreDBDB)
    cursor = connection.cursor()
    sql = sqlQuery
    
    #execute sql query and make csv file for each record
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
