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
<h2>TYPE YOUR QUERY!!!:-</h2>
<p></p>
'''
print yyy
#user=int(data.getvalue('p'))
#print user

#i=user
#pi=ip[user-1]
pi='192.168.10.102'
g=open('dockernamenode','r')
di=g.read()
g.close()
print"namenode"
print pi
print di
