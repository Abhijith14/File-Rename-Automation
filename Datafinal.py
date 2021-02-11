import pandas

import mysql.connector
from mysql.connector import Error


dt = pandas.read_excel(r'C:\Users\ABHIJITH UDAYAKUMAR\PycharmProjects\filerenameAutomation\Data\Whatsapp - XII.xlsx', sheet_name="CORRECTED")

adno = dt['admission'].tolist()
wp = dt['whatsapp'].tolist()

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='jyothisclassdata',
                                         user='root',
                                         password='')
    if connection.is_connected():
        cursor = connection.cursor()
        for i in range(len(adno)):
            print(str(adno[i])+" "+str(wp[i]))
            sql = "UPDATE data SET WHATSAPP_NO =" + str(wp[i]) + " WHERE ADMISSION_NO=" + str(adno[i])
            cursor.execute(sql)
            print(cursor)
        connection.commit()

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")


#print(len(adno))
#print(len(wp))

#def funct():
#    sql_select_Query = "select * from data"
#    cursor = connection.cursor()
#    cursor.execute(sql_select_Query)
#    records = cursor.fetchall()
#    print("Total number of rows in Laptop is: ", cursor.rowcount)#

#    print("\nPrinting each laptop record")
#    for row in records:
#        print()
#        print("Appending ", row[4], )
#        print("Admission Number = ", row[1])

#        mycursor = connection.cursor()

 #       sql = "UPDATE data SET WHATSAPP_NO =" + str(row[1]) + " WHERE ADMISSION_NO=" + str(row[1])

 #       mycursor.execute(sql)

  #      connection.commit()