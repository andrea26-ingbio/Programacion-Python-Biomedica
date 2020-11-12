# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 18:11:37 2020

@author: 1
"""

from tkinter import *
from tkinter.ttk import *
import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="covid-19"
    )

#Pantalla
windows=Tk()
windows.title("COVID-19, Estados de Mexico")
windows.geometry("800x600")
foto=PhotoImage(file='covid.png')
fondo=Label(windows,image=foto).place(x=0, y=0)

selected=IntVar()

#Definir click y cada estado
def click():
    print('         Enfermos','Recuperados','Muertes')
    
    if selected.get()==1:
        mycursor=mydb.cursor()
        
        sql="SELECT \
            estados.Estado AS ala,\
            datos.Enfermos AS fav, \
            datos.Recuperados AS ele, \
            datos.Muertes AS fov \
            FROM estados \
            INNER JOIN datos ON estados.Control=datos.Control where datos.Control='1'"
            
        mycursor.execute(sql)
        myresult=mycursor.fetchall()

        for x in myresult:
            print(x)
        
    elif selected.get()==2:
        mycursor=mydb.cursor()
        
        sql="SELECT \
            estados.Estado AS ala,\
            datos.Enfermos AS fav, \
            datos.Recuperados AS ele, \
            datos.Muertes AS fov \
            FROM estados \
            INNER JOIN datos ON estados.Control=datos.Control where datos.Control='2'"
            
        mycursor.execute(sql)
        myresult=mycursor.fetchall()
        
        for x in myresult:
            print (x)


    elif selected.get()==3:
        mycursor=mydb.cursor()
        
        sql="SELECT \
            estados.Estado AS ala,\
            datos.Enfermos AS fav, \
            datos.Recuperados AS ele, \
            datos.Muertes AS fov \
            FROM estados \
            INNER JOIN datos ON estados.Control=datos.Control where datos.Control='3'"
            
        mycursor.execute(sql)
        myresult=mycursor.fetchall()
        
        for x in myresult:
            print (x)

    elif selected.get()==4:
        mycursor=mydb.cursor()
        
        sql="SELECT \
            estados.Estado AS ala,\
            datos.Enfermos AS fav, \
            datos.Recuperados AS ele, \
            datos.Muertes AS fov \
            FROM estados \
            INNER JOIN datos ON estados.Control=datos.Control where datos.Control='4'"
            
        mycursor.execute(sql)
        myresult=mycursor.fetchall()
        
        for x in myresult:
            print (x)

    else:
        mycursor=mydb.cursor()
        
        sql="SELECT \
            estados.Estado AS ala,\
            datos.Enfermos AS fav, \
            datos.Recuperados AS ele, \
            datos.Muertes AS fov \
            FROM estados \
            INNER JOIN datos ON estados.Control=datos.Control where datos.Control='5'"
            
        mycursor.execute(sql)
        myresult=mycursor.fetchall()
        
        for x in myresult:
            print (x)
        
def cerrar():
     windows.destroy()

boton1=Radiobutton(windows,text="Veracruz",value=1, variable=selected)
boton2=Radiobutton(windows,text="Coahuila",value=2, variable=selected)
boton3=Radiobutton(windows,text="Michoacán",value=3, variable=selected)
boton4=Radiobutton(windows,text="Sonora",value=4, variable=selected)
boton5=Radiobutton(windows,text="Jalisco",value=5, variable=selected)
boton6=Button(windows,text="Enter",command=click)
boton7=Button(windows, text="Salir",command=cerrar)

boton1.grid(column=400,row=20)
boton2.grid(column=400,row=50)
boton3.grid(column=400,row=80)
boton4.grid(column=400,row=110)
boton5.grid(column=400,row=140)
boton6.grid(column=500,row=50)
boton7.grid(column=500,row=100)

windows.mainloop()
