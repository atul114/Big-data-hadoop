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
<h2>YOUR OPTIONS ARE:-</h2>
'''
print yyy
f=open('@dataipinstance','w')
nd=int(data.getvalue('nd'))
print '<pre>'

for i in range(0,nd):
	kk= commands.getoutput('sudo aws ec2 run-instances --image-id ami-f9ada180 --count 1 --instance-type t2.micro --key-name 2ndjune --security-groups launch-wizard-5 --query "Instances[0].InstanceId"')
	print kk
	f.write(kk)
	f.write('\n')
f.close()
print '</pre>'
print '<div class="container">'
print '<form method="post" action="/cgi-bin/@m3.py">'
print '<label>'
print '<input type="submit" value="Click to Configure!!">'
print '</label>'
print '</form>'
print '</div>'





