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
<h2></h2>
'''
print yyy
a=open('@ippu','w')
b=open('@ippv','w')
f=open('@nameipinstance','r')
kk=f.read()
ss=kk[1:-1]
f.close()
print ss

nipu= commands.getoutput("sudo aws ec2 describe-instances --instance-ids "+ss+" --query 'Reservations[0].Instances[0].PublicIpAddress'")
nipv= commands.getoutput("sudo aws ec2 describe-instances --instance-ids "+ss+" --query 'Reservations[0].Instances[0].PrivateIpAddress'")
nipu=nipu[1:-1]
nipv=nipv[1:-1]
a.write(nipu)
b.write(nipv)
a.write('\n')
b.write('\n')
print nipu
print nipv

print '<h2><u><b> <span style="color:red">YOUR NAMENODE IS  </span></b></u> :- </h2>'
print '<h2>'
print nipu 
print '</h2>'
g=open('@dataipinstance','r')
dataip=g.read().splitlines()
g.close()
print dataip
print '<h2><u><b> <span style="color:red">YOUR DATANODES ARE </span></b></u>:-'
print '</h2>'
j=1;
for ii in dataip:
	ii=ii[1:-1]
	nipu= commands.getoutput("sudo aws ec2 describe-instances --instance-ids "+ii+" --query 'Reservations[0].Instances[0].PublicIpAddress'")
	nipv= commands.getoutput("sudo aws ec2 describe-instances --instance-ids "+ii+" --query 'Reservations[0].Instances[0].PrivateIpAddress'")
	nipu=nipu[1:-1]
	nipv=nipv[1:-1]
	a.write(nipu)
	b.write(nipv)
	a.write('\n')
	b.write('\n')
	print "<h2>"	
	print j
	print ")&nbsp&nbsp&nbsp&nbsp&nbsp"
	j=j+1
	print nipu
	print '</h2>'
a.close()
b.close()
f.close()


print '<div class="container">'
print '<br><br>'
print '<form method="post" action="/cgi-bin/@m4.py">'
print '<label>'
print '<input type="submit" value="Click to Set meta directories!!">'
print '</label>'
print '</form>'
print '</div>'











