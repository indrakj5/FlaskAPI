import mysql.connector

conn = mysql.connector.connect(host='localhost',
                                database = 'mahasiswa',
                                user='root',
                                password='indrakj')

cur = conn.cursor()