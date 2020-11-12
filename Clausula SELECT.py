# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 16:02:03 2020

@author: 1
"""

import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="directorio"
    )

mycursor=mydb.cursor()
mycursor.execute("SELECT * FROM alumnos")
myresult=mycursor.fetchall()

for x in myresult:
    print(x)