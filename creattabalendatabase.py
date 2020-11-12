# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 13:13:23 2020

@author: 1
"""

import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Directorio"
    )

mycursor=mydb.cursor()

mycursor.execute("CREATE TABLE Alumnos (Nombre VARCHAR(255), Email VARCHAR(255))")