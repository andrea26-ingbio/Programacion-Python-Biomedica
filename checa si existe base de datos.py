# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 13:41:44 2020

@author: 1
"""

import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
    )

mycursor=mydb.cursor()
mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x)