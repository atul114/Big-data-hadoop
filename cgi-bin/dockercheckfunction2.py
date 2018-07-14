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
u1=data.getvalue('1')
u2=data.getvalue('2')
u3=data.getvalue('3')
u4=data.getvalue('4')
u5=data.getvalue('5')
print u1
#print commands.getoutput("sshpass -p 'q' ssh -o StrictHostKeyChecking=no root@"+pi+" sudo fallocate -l "+u3+"M "+u1)
print commands.getoutput(" sudo docker exec "+di+" fallocate -l "+u3+"M "+u1)
print commands.getoutput(" sudo docker exec "+di+" hadoop fs -Ddfs.replication="+u4+" -Ddfs.block.size="+u5+"  -put "+u1+" "+u2)
print '<form method="post" action="/cgi-bin/dockercheck4.py">'
print '<label><input type="submit" value="Click to perform more"></label>'
print '</form>'





