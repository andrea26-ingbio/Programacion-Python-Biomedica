# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 13:43:45 2020

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
mycursor.execute("SHOW TABLES")

for x in mycursor:
    print(x)