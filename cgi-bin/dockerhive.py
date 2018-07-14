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
print yyy


#ip=['192.168.10.102','192.168.10.103']
pi='192.168.10.102'
g=open('dockernamenode','r')
di=g.read()
g.close()
h=open('numberdata','r')
nd=h.read()
h.close()
#print  ip
#print"namenode"
#print pi
print commands.getoutput(" sudo docker exec "+di+' hive')
print time.sleep(50)
print commands.getoutput(" sudo docker exec "+di+' hadoop fs -chmod 777 /tmp/hive')
print time.sleep(20)
print commands.getoutput(" sudo docker exec "+di+' hive')
print commands.getoutput(" sudo docker exec "+di+' hadoop fs -chmod 777 /tmp/hive')
print commands.getoutput(" sudo docker exec "+di+' hive')
print time.sleep(20)
print commands.getoutput(" sudo docker exec "+di+' hadoop fs -chmod 777 /tmp/hive')
print commands.getoutput(" sudo docker exec "+di+' hive')
print time.sleep(20)
print commands.getoutput(" sudo docker exec "+di+' hadoop fs -chmod 777 /tmp/hive')


print commands.getoutput(" sudo docker exec "+di+' hive')

 


























