import random
import string
import mysql.connector
from mysql.connector import Error

def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='jyothisclassdata',
                                         user='root',
                                         password='')
    if connection.is_connected():
        sql_select_Query = "select * from data"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        print("Total number of rows is: ", cursor.rowcount)

        print("\nPrinting each record")
        for row in records:
            print()
            print("Appending ", row[4], )
            print("Admission Number = ", row[1])
            mycursor = connection.cursor()
            code = get_random_string(6)
            print(code)
            sql = "UPDATE admin SET VCODE ='" + code + "' WHERE ADNO=" + str(row[1])
            print(sql)
            mycursor.execute(sql)

            connection.commit()

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")