#!/usr/bin/python

import  cgi
import time
import commands
import os

print  "content-type:text/html"
print  ""
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
<p></p>
'''
print '<pre>'
#f=open('i','w')
#f.write( commands.getoutput('sudo aws ec2 describe-instances | grep PublicIpAddress | grep -o -P "\d+\.\d+\.\d+\.\d+" | grep -v "^10\."'))
#print commands.getoutput('sudo aws ec2 describe-instances --region us-west-2 --output table')
#print commands.getoutput('sudo aws ec2 describe-instances | grep PublicIpAddress | grep -o -P "\d+\.\d+\.\d+\.\d+" | grep -v "^10\."')
#print commands.getoutput('aws ec2 run-instances --image-id ami-6f68cf0f --count 1 --instance-type t2.micro --key-name 2ndjune --security-group-ids launch-wizard-5 --region us-west-2')
#f.close()
kk= commands.getoutput('sudo aws ec2 run-instances --image-id ami-09939f70 --count 1 --instance-type t2.micro --key-name 2ndjune --security-groups launch-wizard-5 --query "Instances[0].InstanceId" ')
f=open('@nameipinstance','w')
f.write(kk)
f.close()
print '</pre>'
print '<div class="container">'
print '<form method="post" action="/@data1.html">'
print '<label>'
print '<input type="submit" value="Click to Start the creation of Data nodes!!">'
print '</label>'
print '</form>'
print '</div>'


















