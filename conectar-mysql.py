# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 13:09:52 2020

@author: 1
"""

import mysql.connector

mydb=mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password=""
    )

print(mydb)