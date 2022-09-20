# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 13:51:34 2019

@author: /Rook
C:\Git\RES\res.py
"""

import pandas as pd
from tkinter import Tk, Button, Frame  #, Label
from PIL import ImageTk  
import os
#import cv2

img={}
c=[]
def Command0(i):
    print(i)
    c.append(int(i))
    fr.destroy()
    return;


def d():
#   направление
#    fr=Frame(root,bg='blue',bd=2)
#    fr.pack()
    k=len([1 for x in list(os.scandir("d/")) if x.is_file()])
#   Label(fr1,text='Выберите направление').pack()
    for i in range(1, k+1):
        ft="d/d"+str(i)+".jpg"
        img[i] = ImageTk.PhotoImage(file=ft)
        Button(fr, image=img[i], command=lambda i=i: Command0(i)).pack(side = 'left')
#    df = pd.read_csv('DB/acc.csv', sep = ';')
#    print(df)



root = Tk()

fr=Frame(root,bg='blue',bd=2)
fr.pack()

d()

root.mainloop()

