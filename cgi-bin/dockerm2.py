#!/usr/bin/python2
import  cgi
import time
import commands
import os

print  "content-type:text/html"
print  ""
data=cgi.FieldStorage()
print data
nd=int(data.getvalue('nd'))
kl=str(nd)
f=open('numberdata','w')
f.write(kl)
f.close()
yyy='''
<head>
  <title>List of services provided : </title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="/static/c1.css">
  <script src="/static/j2.js"></script>
  <script src="/static/j3.js"></script>
</head>
<style type="text/css">
body{
background-color: #b0e0e6;
padding 20px;
}
</style>
<body>
<div class="container">
<h2>YOUR OPTIONS ARE:-</h2>
'''
print yyy
print '<pre>'

for i in range(0,nd):
	kk= commands.getoutput('sudo docker run -itd 511de34f6da2')
	print kk
print '</pre>'
print '<div class="container">'
print '<form method="post" action="/cgi-bin/dockerm3.py">'
print '<label>'
print '<input type="submit" value="Click to Configure!!">'
print "<input type ='hidden' name='nd' value="+str(nd)+">"
print '</label>'
print '</form>'
print '</div>'





