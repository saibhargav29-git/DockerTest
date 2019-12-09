#!/usr/bin/python3
from __future__ import print_function
from tkinter import *
import tkinter as tk
import paramiko
import sys
import os
import sqlite3
from sys import argv
import time
import datetime
bundle_dir = 'hi'
ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d-%H-%M-%S')
fields = 'FedEx ID', 'Password'
level = ['L1', 'L2', 'L3', 'L4','L5', 'L6','Prod','CL','SB']
app = ['GUI', 'WFL', 'TRANS', 'ESOT','SMS','TMS','DIR','FTIP','TRANS','GUI-Cloud','ZWEB','CASH']

def fetch(entries):
   bundle_dir = sys.argv[0]
   print (bundle_dir)
   i = 2
   username=''
   password=''
   for entry in entries:
      field = entry[0]
      text  = entry[1].get()
      if (i%2==0):
         username = text
         i=i+1
      else:
         password = text
   p1 = var.get()
   p2 = var1.get()
   connectiondb = bundle_dir+'test.db'
   print(connectiondb)
   conn = sqlite3.connect(connectiondb)
   cursor = conn.execute("SELECT URL from SERVERS where LEVEL=? and APP=?",(p1, p2))
   for row in cursor:
      opens=row[0]
   conn.close()
   string = opens
   cut_string = string.split('//')
   new_string = cut_string[1]
   temp = new_string.split(':')
   server = temp[0]
   ip= server
   port=22
   ssh=paramiko.SSHClient()
   ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
   ssh.connect(ip,port,username,password)
   stdin,stdout,stderr=ssh.exec_command("ps -ef | grep java")
   outlines=stdout.readlines()
   resp=''.join(outlines)
   f = open('temp.txt', 'a+')
   f.write(resp) 
   f.close()
   convert = bundle_dir+'/txt2pdf.py temp.txt'
   print (convert)
   os.system(convert)
   rename = 'rename temp.pdf'+' '+p2+p1+st+'.pdf'
   os.system(rename)
   os.system('del temp.txt')   
def makeform(root, fields):
   entries = []
   i = 2
   for field in fields:
      row = Frame(root)
      lab = Label(row, width=15, text=field, anchor='w')
      if (i%2==0):
         ent = Entry(row)
         i=i+1
      else:
         ent = Entry(row,show="*")
      row.pack(side=TOP, fill=X, padx=5, pady=5)
      lab.pack(side=LEFT)
      ent.pack(side=RIGHT, expand=YES, fill=X)
      entries.append((field, ent))
   return entries

if __name__ == '__main__':
   root = tk.Tk()
   root.geometry("%dx%d+%d+%d" % (600, 300, 50, 50))
   ents = makeform(root, fields)
   var1 = tk.StringVar(root)
   var1.set('Application')
   app = ['GUI', 'WFL', 'TRANS', 'ESOT','SMS','TMS','DIR','FTIP','TRANS','GUI-Cloud','ZWEB','CASH']
   option =tk.OptionMenu(root, var1, *app)
   option.pack(side='left', padx=50, pady=50)
   option.config(bg='purple', fg='white', font = ('Sans','10','bold'))
   option["menu"].config(bg='white')
   var = tk.StringVar(root)
   var.set('Level')
   level = ['L1', 'L2', 'L3', 'L4','L5', 'L6','Prod','CL','SB']
   option = tk.OptionMenu(root, var, *level)
   option.config(bg='purple', fg='white', font = ('Sans','10','bold'))
   option["menu"].config(bg='white')
   option.pack(side='left', padx=50, pady=50)

   root.bind('<Return>', (lambda event, e=ents: fetch(e)))
   b1 = Button(root, text='GenerateReport', bg='purple',
          command=(lambda e=ents: fetch(e)))
   b1.config(fg='white', font = ('Sans','10','bold'))
   b1.pack(side=LEFT, padx=5, pady=5)
   root.mainloop()
