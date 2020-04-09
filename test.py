import csv
import MySQLdb

covid19 = MySQLdb.connect(host='localhost',
    user='root',
    passwd='',
    db='covid19')
cursor = covid19.cursor()
csv_data = csv.reader(open('covid_19_data.csv'))
for row in csv_data:

    cursor.execute('INSERT INTO countries(SNo, ObservationDate, Province_State, Country_Region, Last_Update, Confirmed, Deaths, Recovered )' \
          'VALUES("%s", STR_TO_DATE("%s","%d/%m/%Y"), "%s", "%s", "%s", "%s", "%s", "%s")', 
          row)
#close the connection to the database.
covid19.commit()
cursor.close()
print ("Done")
