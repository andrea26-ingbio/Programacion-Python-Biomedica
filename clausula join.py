# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 16:25:42 2020

@author: 1
"""

import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="covid-19"
    )

mycursor=mydb.cursor()

sql="SELECT \
    estados.Estado AS ala,\
    datos.Enfermos AS fav, \
    datos.Recuperados AS ele, \
    datos.Muertes AS fov \
    FROM estados \
    INNER JOIN datos ON estados.Control=datos.Control"
    
mycursor.execute(sql)
myresult=mycursor.fetchall()

for x in myresult:
    print(x)