'''
Created on Sep 11, 2017

@author: admin_home
'''
import os
import time
import json
# converting the 50 web pages into a cdr file
f_path = raw_input('Enter  path : ')
#f_path='C:\Users\admin_home\eclipse-workspace\python code\test'
cdr={}
cdrfile=open('json.jl','w')
url=[]
html=[]
filenames = os.listdir(f_path)
 
doc_id=1 
for filename in os.listdir(f_path):
    filename1 = filename.replace("%3A",":")
    filename1 = filename1.replace("%2F","/")
    #rl.append(filename1) 
    
    f= open(f_path+"/"+filename,'r')
    readdata=f.read()
    fullpath=os.path.join(f_path, filename)
    timestamp=str(time.ctime(int(os.path.getmtime(fullpath))))
    jsonlines={"doc_id":doc_id,"url":filename1,"raw_content":readdata,"timestamp":timestamp}
    cdrobj=json.dumps(dict(jsonlines))+"\n"
    cdrfile.write(cdrobj)
    doc_id+=1
    if doc_id == 51:
        break
    
cdrfile.close()