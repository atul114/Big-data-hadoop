#!/usr/bin/python2
import  cgi
import time
import commands
import os

print  "content-type:text/html"
print  ""
data=cgi.FieldStorage()
print data
yyy='''
<head>
  <title>List of services provided : </title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="/static/c1.css">
  <script src="/static/j2.js"></script>
  <script src="/static/j3.js"></script>
</head>
<body>
<div class="container">
<h2>YOUR OPTIONS ARE:-</h2>
<p>Choose the desired</p>
'''
print yyy
g=open('dockernamenode','r')
di=g.read()
g.close()
g=open('/var/www/html/dockerloc','r')
loc=g.read().splitlines()
g.close()
print loc[0]
print loc[1]
print loc[2]
print loc[3]

#print commands.getoutput(" sshpass -p 'q' ssh -o StrictHostKeyChecking=no root@" +pi+' sudo hadoop fs -mkdir /sample')
print '<pre>'
print commands.getoutput("sudo docker exec "+di+' hadoop fs -Ddfs.replication='+loc[1]+' -Ddfs.block.size='+loc[2]+' -put '+loc[0]+' '+loc[3])
print '</pre>'
print '<form method="post" action="/cgi-bin/dockercheck4.py">'
print '<label><input type="submit" value="Click to perform more"></label>'
print '</form>'





