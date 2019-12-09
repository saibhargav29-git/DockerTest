import webbrowser
import sqlite3
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import datetime

bundle_dir = sys._MEIPASS
try:
    # Python2
    import Tkinter as tk
except ImportError:
    # Python3
    import tkinter as tk
def select():
                p1 = var.get()
                p2 = var1.get()
                connection=bundle_dir+'/test.db'
                conn = sqlite3.connect(connection)
                cursor = conn.execute("SELECT URL from SERVERS where LEVEL=? and APP=?",(p1, p2))
                for row in cursor:
                        open=row[0]
                conn.close()
                if p2 == "GUI":
                    password = "wlsadmin01"
                else:
                    password = "wlsadmin1"
                username = "weblogic"
                chrome = bundle_dir+"/chromedriver.exe"
                driver = webdriver.Chrome(chrome)
                driver.get(open)
                driver.find_element_by_id("j_username").send_keys(username)
                driver.find_element_by_name("j_password").send_keys(password)
                driver.find_element_by_xpath("""//*[@id="loginData"]/div[4]/span/input""").click()
                driver.find_element_by_xpath("""//*[@id="HomePagePortlet"]/div/div[6]/div[2]/ul/li[1]/a""").click()
                #root.title("Opening "+open)             
                #webbrowser.open_new_tab(open)
                
def printing():
                p1 = var.get()
                p2 = var1.get()
                connection=bundle_dir+'/test.db'
                conn = sqlite3.connect(connection)
                cursor = conn.execute("SELECT URL from SERVERS where LEVEL=? and APP=?",(p1, p2))
                for row in cursor:
                        open=row[0]
                conn.close()
                string = open
                cut_string = string.split('//')
                new_string = cut_string[1]
                temp = new_string.split(':')
                server = temp[0]
                #w = tk.Label(root, text=p2 + '-' + p1 + ':' + server)
                #w.pack(side='left')    
                var2.set(p2 + '-' + p1 + ':' + server)

def screenshot():
                p1 = var.get()
                p2 = var1.get()
                ts = time.time()
                st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d-%H-%M-%S')
                print(st)
                if p2 == "GUI":
                    password = "wlsadmin01"
                else:
                    password = "wlsadmin1"
                username = "weblogic"   
                connection=bundle_dir+'/test.db'
                conn = sqlite3.connect(connection)
                cursor = conn.execute("SELECT URL from SERVERS where LEVEL=? and APP=?",(p1, p2))
                for row in cursor:
                        open=row[0]
                conn.close()
                chrome = bundle_dir+"/chromedriver.exe"
                driver = webdriver.Chrome(chrome)
                driver.get(open)
                driver.find_element_by_id("j_username").send_keys(username)
                driver.find_element_by_name("j_password").send_keys(password)
                driver.find_element_by_xpath("""//*[@id="loginData"]/div[4]/span/input""").click()
                driver.find_element_by_xpath("""//*[@id="HomePagePortlet"]/div/div[6]/div[2]/ul/li[1]/a""").click()
                driver.save_screenshot(p2+"_"+p1+"_"+st+"_servers.png")
                time.sleep(2)
                driver.find_element_by_xpath("""//*[@id="topMenu"]/ul/li[1]/a""").click()
                driver.find_element_by_xpath("""//*[@id="HomePagePortlet"]/div/div[6]/div[3]/ul/li/a""").click()
                driver.save_screenshot(p2+"_"+p1+"_"+st+"_deployments.png")
                for i in range(1, 10):
                    id = str(i)
                    path_dep="""//*[@id="state"""+id+""""]/a"""
                    try:
                        driver.find_element_by_xpath(path_dep).click()
                        driver.save_screenshot(p2+"_"+p1+"_"+st+"_deployment_"+id+".png")
                        driver.find_element_by_xpath("""//*[@id="topMenu"]/ul/li[1]/a""").click()
                        driver.find_element_by_xpath("""//*[@id="HomePagePortlet"]/div/div[6]/div[3]/ul/li/a""").click()
                    except:
                        break
                foldername = p2+"_"+p1+"_"+st
                createfolder = "mkdir " +foldername
                os.system(createfolder)
                cwd = os.getcwd()
                cwd = cwd + "\\"
                copyfolder = "move "+cwd+"*.png " +cwd +foldername
                print (copyfolder)
                os.system(copyfolder)
def report():
             cmdstring=bundle_dir+"/gui.py "+bundle_dir
             print (cmdstring)
             os.system(cmdstring)
    
root = tk.Tk()
# use width x height + x_offset + y_offset (no spaces!)
root.geometry("%dx%d+%d+%d" % (1180, 640, 50, 50))
root.configure(background='white')
root.title("Application")
var = tk.StringVar(root)
var2 = tk.StringVar(root)
var3 = tk.StringVar(root)
#var4 = tk.StringVar(root)

var3.set('FedEx_SalesITDevSecOps')
label1 = tk.Label(root, textvariable=var3,bg='purple',fg='white')
label1.config(font=("courier",'15'))
label1.pack(anchor='n',pady=50)

var2.set('Server name')
label3 = tk.Label(root, textvariable=var2,bg='purple',fg='white')
label3.config(font=("courier",'15'))
label3.pack( anchor='n',padx=50, pady=30)

# initial value
var.set('Level')
level = ['L1', 'L2', 'L3', 'L4','L5', 'L6','Prod','CL','SB']
option = tk.OptionMenu(root, var, *level)
option.config(bg='purple', fg='white', font = ('Sans','10','bold'))
option["menu"].config(bg='white')
option.pack(side='left', padx=50, pady=50)
# initial value
var1 = tk.StringVar(root)
var1.set('Application')
app = ['GUI', 'WFL', 'TRANS', 'ESOT','SMS','TMS','DIR','FTIP','TRANS','GUI-Cloud','ZWEB','CASH']
option = tk.OptionMenu(root, var1, *app)
option.pack(side='left', padx=50, pady=50)
option.config(bg='purple', fg='white', font = ('Sans','10','bold'))
option["menu"].config(bg='white')
button = tk.Button(root, text="Open", command=select , bg='purple')
button.config(fg='white',font = ('Sans','10','bold'))
button.pack(side='left', padx=50, pady=50)
button1 = tk.Button(root, text="Print Server",command=printing, bg='purple')
button1.config(fg='white', font = ('Sans','10','bold'))
button1.pack(side='left', padx=50, pady=50)
button2 = tk.Button(root, text="Screenshot",command=screenshot, bg='purple')
button2.config(fg='white', font = ('Sans','10','bold'))
button2.pack(side='left', padx=50, pady=50)
button3 = tk.Button(root, text="report app",command=report, bg='purple')
button3.config(fg='white', font = ('Sans','10','bold'))
button3.pack(side='left', padx=50, pady=50)
root.mainloop()
