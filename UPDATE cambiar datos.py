# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 15:37:25 2020

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
sql="UPDATE alumnos SET nombre = 'Maria Palos' WHERE nombre = 'Jose Palos'"

mycursor.execute(sql)

mydb.commit()
print(mycursor.rowcount, "Se cambiio con exito")