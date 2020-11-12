# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 13:48:21 2020

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

sql="INSERT INTO alumnos(Nombre,email) VALUES (%s,%s)"
val=("Jose Palos", "nachitops@hotmail.es")
mycursor.execute(sql,val)

mydb.commit()
print(mycursor.rowcount,"Alumno agregado.")