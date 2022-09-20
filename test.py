# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 15:28:10 2019

@author: 1
"""


#import os
#import cv2
#
#instances = []
## Load in the images
#for filepath in os.listdir('f/'):
#    instances.append(cv2.imread('f/{0}'.format(filepath),0))
#print((instances[0]))


#import numpy as np
#import glob
#fl = glob.glob('f/*.*')
##fl = 'f1.jpg', 'f2.jpg', 'f3.jpg', 'f4.jpg'
#print(fl[0])
##x = np.array([np.array(Image.open(fname)) for fname in fl])
#
#from PIL import Image, ImageDraw
#text = "Hello, PIL!!!"
#color = (0, 0, 120)
#img = Image.new('RGB', (100, 50), color)
#imgDrawer = ImageDraw.Draw(img)
#imgDrawer.text((10, 20), text)
#img.save("pil-basic-example.png")

import tkinter
from PIL import Image, ImageTk
import numpy

#class mainWindow():
#    def __init__(self):
#        self.root = tkinter.Tk()
#        self.frame = tkinter.Frame(self.root, width=500, height=400)
#        self.frame.pack()
#        self.canvas = tkinter.Canvas(self.frame, width=500,height=400)
#        self.canvas.place(x=-2,y=-2)
#        data=numpy.array(numpy.random.random((400,500))*100,dtype=int)
#        
#        self.im=Image.frombytes('L', (data.shape[1],data.shape[0]), data.astype('b').tostring())
#        self.photo = ImageTk.PhotoImage(image=self.im)
#        self.canvas.create_image(0,0,image=self.photo,anchor=tkinter.NW)
#        self.root.update()
#        self.root.mainloop()
#
#mainWindow()


root = tkinter.Tk()
frame = tkinter.Frame(root, width=500, height=400)
frame.pack()
canvas = tkinter.Canvas(frame, width=500,height=400)
canvas.place(x=-2,y=-2)
data=numpy.array(numpy.random.random((400,500))*100000,dtype=int)
print(data)
im=Image.frombytes('L', (data.shape[1],data.shape[0]), data.astype('b').tostring())
photo = ImageTk.PhotoImage(image=im)
canvas.create_image(0,0,image=photo,anchor=tkinter.NW)

root.update()
root.mainloop()

