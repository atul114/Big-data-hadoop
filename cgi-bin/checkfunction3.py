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
g=open('nameip','r')
pi=g.read()
g.close()
u1=data.getvalue('1')
u2=data.getvalue('2')
u3=data.getvalue('3')
u4=data.getvalue('4')
print u1
print pi
#print commands.getoutput("sshpass -p 'q' ssh -o StrictHostKeyChecking=no root@"+pi+" sudo fallocate -l "+u3+"M "+u1)
#print commands.getoutput(" sshpass -p 'q' ssh -o StrictHostKeyChecking=no root@"+pi+" sudo fallocate -l "+u3+"M "+u1)
print commands.getoutput(" sshpass -p 'q' ssh -o StrictHostKeyChecking=no root@"+pi+" sudo hadoop fs -Ddfs.replication="+u3+" -Ddfs.block.size="+u4+"  -put "+u1+" "+u2)
print '<form method="post" action="/cgi-bin/check4.py">'
print '<label><input type="submit" value="Click to perform more"></label>'
print '</form>'





