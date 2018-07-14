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
<style type="text/css">
body{
background-color: #b0e0e6;
padding 20px;
}
</style>
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
print '<br>'
print '<textarea rows="10" cols="50" name="comment" form="usrform" placeholder="ENTER YOUR TEXT HERE......."></textarea>'
ooo='''<form action="/hivequery.php" type="POST" id="usrform">
  <input type="hidden" name="usrname">
  <input type="submit" value="Submit query">
</form>
<br>'''
print ooo

print '<form method="post" action="/cgi-bin/hivequerystart.py">'
print '<label><input type="submit" value="Click to RESET"></label>'
print '</form>'









