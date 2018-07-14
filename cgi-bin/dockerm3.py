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
<h2></h2>
'''
print yyy

print '<h2><u><b> <span style="color:red">YOUR NAMENODE IS  </span></b></u> :- </h2>'
print '<h2>'
print "172.17.0.2"
print '</h2>'
print '<h2><u><b> <span style="color:red">YOUR DATANODES ARE </span></b></u>:-'
print '</h2>'
j=3;
for i in range(0,nd):
	print '<h2>'
	print '172.17.0.'+str(j)
	print '</h2>'
	print '<br>'
	j=j+1

print '<div class="container">'
print '<br><br>'
print '<form method="post" action="/cgi-bin/dockercheck4.py">'
print '<label>'
print '<input type="submit" value="Click to Set meta directories!!">'
print '</label>'
print '</form>'
print '</div>'











