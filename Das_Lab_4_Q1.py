# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 10:20:38 2021

@author: siddh
"""
# to import the tkinter module for GUI toolkit
import tkinter
import math # importing tkinter and math python modules
class Hypotenuse:

    def __init__(self):

        self.window = tkinter.Tk() # creating the main window

        self.window.title("Right Triangle Calculator") # setting window title

        self.window.geometry("400x100") # setting window dimensions

        self.AFrame = tkinter.Frame(self.window)

        self.BFrame = tkinter.Frame(self.window)

        self.CFrame = tkinter.Frame(self.window)

        self.ansFrame = tkinter.Frame(self.window)

        self.butFrame = tkinter.Frame(self.window) # creating the five frames

        self.ALabel = tkinter.Label(self.AFrame, text=' Side A:')

        self.AEntry = tkinter.Entry(self.AFrame, width = 30)

        self.ALabel.pack(side = 'left')

        self.AEntry.pack(side = 'left') # creating a label and entry field for side A

        self.BLabel = tkinter.Label(self.BFrame, text = ' Side B:')

        self.BEntry = tkinter.Entry(self.BFrame, width = 30)

        self.BLabel.pack(side = 'left')

        self.BEntry.pack(side = 'left') # creating a label and entry field for side B
        
        self.CLabel = tkinter.Label(self.CFrame, text = ' Side C:')
        
        self.CEntry = tkinter.Entry(self.CFrame, width = 30)
        
        self.CLabel.pack(side = 'left')
        
        self.CEntry.pack(side = 'left') # creating a label and entry field for side C
        
        self.quitBut = tkinter.Button(self.butFrame, text = 'Exit', command = self.window.destroy) # quiting application on clicking this
        
        self.calcBut = tkinter.Button(self.butFrame, text = 'Calculate', command = self.CalcAns) # calling CalcAns on clicking this
        
        self.quitBut.pack(side = 'right')
        
        self.calcBut.pack(side = 'right')
        
        self.AFrame.pack()
        
        self.BFrame.pack()
        
        self.CFrame.pack()
        
        self.ansFrame.pack()
        
        self.butFrame.pack()
        
        tkinter.mainloop() # to start the application


    def CalcAns(self):

        self.A = float(self.AEntry.get())

        self.B = float(self.BEntry.get()) # getting the values from A and B entry labels

        self.CEntry.insert(tkinter.INSERT, str(round((math.sqrt(self.A ** 2 + self.B ** 2)), 3))) # calculating and inserting in C entry label
Hypo = Hypotenuse()         