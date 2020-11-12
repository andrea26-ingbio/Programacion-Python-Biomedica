# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 17:42:24 2020

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
sql="DELETE FROM alumnos WHERE nombre='Maria Palos'"
mycursor.execute(sql)
mydb.commit()

print(mycursor.rowcount, "Eliminado")