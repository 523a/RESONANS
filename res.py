# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 20:08:25 2019

@author: /Rook
"""
# -*- coding: utf-8 -*-
#!/usr/bin/env python3

#from __future__ import (absolute_import, division,
#                        print_function, unicode_literals)
## отключим предупреждения Anaconda
#import warnings 
#warnings.simplefilter('ignore')
import pandas as pd
import os, os.path

#import numpy as np

from tkinter import Tk, Button, Frame  #, Label
from PIL import ImageTk
  
img={}
c=[]

def Command0(i):
    print(i)
    c.append(int(i))
    fr1.destroy()
    f()
    return;

def Command1(i):
    print(i)
    c.append(int(i))
    fr2.destroy()
    w()

def Command2(i):
    print(i)
    c.append(int(i))
    fr3.destroy()
    t()
    
def Command3(i):
    print(i)
    c.append(int(i))
    fr4.destroy()
    e()
    
def Command4(i):
    print(i)
    c.append(int(i))
    fr5.destroy()
    a()
    
def Command5(i):
    print(i)
    c.append(int(i))
    fr6.destroy()
    l()
    
def Command6(i):
    print(i)
    c.append(int(i))
    fr7.destroy()
    l()

def d():
#   направление
    k=len([1 for x in list(os.scandir("d/")) if x.is_file()])
#   Label(fr1,text='Выберите направление').pack()
    for i in range(1, k+1):
        ft="d/d"+str(i)+".jpg"
        img[i] = ImageTk.PhotoImage(file=ft)
        Button(fr1, image=img[i], command=lambda i=i: Command0(i)).pack(side = 'left')
    
def f():
#   фюзеляж
    k=len([1 for x in list(os.scandir("f/")) if x.is_file()])
    for i in range(1, k+1):
        ft="f/f"+str(i)+".jpg"
        img[i] = ImageTk.PhotoImage(file=ft)
        Button(fr2, image=img[i], command=lambda i=i: Command1(i)).pack(side = 'left')

def w():
#   крылья
    k=len([1 for x in list(os.scandir("w/")) if x.is_file()])
    for i in range(1, k+1):
        ft="w/w"+str(i)+".jpg"
        img[i] = ImageTk.PhotoImage(file=ft)
        Button(fr3, image=img[i], command=lambda i=i: Command2(i)).pack(side = 'left')

def t():
#   хвост
    k=len([1 for x in list(os.scandir("t/")) if x.is_file()])
    for i in range(1, k+1):
        ft="t/t"+str(i)+".jpg"
        img[i] = ImageTk.PhotoImage(file=ft)
        Button(fr4, image=img[i], command=lambda i=i: Command3(i)).pack(side = 'left')
    
def e():
#   двигатель
    k=len([1 for x in list(os.scandir("e/")) if x.is_file()])
    for i in range(1, k+1):
        ft="e/e"+str(i)+".jpg"
        img[i] = ImageTk.PhotoImage(file=ft)
        Button(fr5, image=img[i], command=lambda i=i: Command4(i)).pack(side = 'left')

def a():
#   аэлероны
    k=len([1 for x in list(os.scandir("a/")) if x.is_file()])
    for i in range(1, k+1):
        ft="a/a"+str(i)+".jpg"
        img[i] = ImageTk.PhotoImage(file=ft)
        Button(fr6, image=img[i], command=lambda i=i: Command5(i)).pack(side = 'left')

def l():
#   самолеты
    k=len([1 for x in list(os.scandir("DB/aircrafts/")) if x.is_file()])
    for i in range(1, k+1):
        ft="DB/aircrafts/A"+str(i)+".jpg"
        img[i] = ImageTk.PhotoImage(file=ft)
        Button(fr7, image=img[i], command=lambda i=i: Command6(i)).pack(side = 'left')

def ll():
#    фильтр по выбранным позиц
    df = pd.read_csv('DB/acc.csv', sep = ';')
    print(df)


root = Tk()

root.title("Выбор")
    

fr1=Frame(root,bg='blue',bd=2)
fr1.pack()
fr2=Frame(root,bg='blue',bd=2)
fr2.pack()
fr3=Frame(root,bg='blue',bd=2)
fr3.pack()
fr4=Frame(root,bg='blue',bd=2)
fr4.pack()
fr5=Frame(root,bg='blue',bd=2)
fr5.pack()
fr6=Frame(root,bg='blue',bd=2)
fr6.pack()
fr7=Frame(root,bg='blue',bd=2)
fr7.pack()

d()

root.mainloop()






