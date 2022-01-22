# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 17:42:03 2022

@author: chnt2
"""

import json
import requests

response = requests.get('https://gh-trending-api.herokuapp.com/repositories')
json_data = json.loads(response.text)

print(len(json_data))


pr={}

for a in json_data:
    if a["language"] in pr:
        pr[a['language']].append(a['username'])
    else:
        pr[a['language']]=[a['username']]
print(pr)
        

import tkinter

from tkinter import *

top = tkinter.Tk()

L1 = Label(top, text="Trending")
L1.pack( side = TOP)
ln=Canvas(top,width=300,height=2,bg='red')
ln.pack()

"""
for c,a in enumerate(json_data):
    p=[a["username"],a["repositoryName"]]
    L12 = Label(top, text="#"+str(c+1))
    L12.pack( side = TOP)   
    L12 = Label(top, text="username"+p[0])
    L12.pack( side = TOP)
    L13= Label(top, text="repositoryName"+p[1])
    L13.pack( side = TOP)
    ln=Canvas(top,width=300,height=2,bg='black')
    ln.pack()"""
text= Text(top)
def opeWindow():
    c=0
    text.delete('1.0',END)
    for a in pr:
        text.insert(INSERT, a+'\n')
        text.grid_columnconfigure(c)
        text.pack()
        
        text.insert(INSERT, "List of People:-"+str(pr[a])+'\n')
        text.grid_columnconfigure(c)
        text.pack()
        text.insert(INSERT, "******************"+'\n')
        text.grid_columnconfigure(c)
        text.pack()
        c=c+1
        
        

def openNewWindow():
    
    text.delete('1.0',END)
        
    for c,a in enumerate(json_data):
        
        text.insert(INSERT, "#"+str(c)+'\n')
        text.grid_columnconfigure(c)
        text.pack()
        
        text.insert(INSERT, "username:"+a["username"]+'\n')
        text.grid_columnconfigure(c)
        text.pack()
        text.insert(INSERT, "repositoryName:"+a["repositoryName"]+'\n')
        text.grid_columnconfigure(c)
        text.pack()
        if str(a["description"])!="None":
            
            text.insert(INSERT, "description:"+a["description"]+'\n')
            text.grid_columnconfigure(c)
            text.pack()
        text.insert(INSERT, "--------------------"+'\n')
        text.grid_columnconfigure(c)
        text.pack()
            

btn = Button(top,text ="Click to the TOP RANKING",command = openNewWindow)
btn.pack(pady = 10)   


btn = Button(top,text ="GRoup By language",command = opeWindow)
btn.pack(pady = 10) 
top.mainloop()
