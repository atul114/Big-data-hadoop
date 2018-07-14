#!/usr/bin/python2
import  cgi
import time
import commands
import os

print  "content-type:text/html"
print  ""
data=cgi.FieldStorage()
#print data
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
<h1><center><span style="color:green"><u>YOUR REQUESTS ARE BEING PROCESSED</u> . . . . .</span></center></h1>
<p></p>
'''
print yyy
time.sleep(3)
g=open('nameip','r')
pi=g.read()
g.close()
u1=data.getvalue('1')
u2=data.getvalue('2')
#print u1
#print pi
#print commands.getoutput("sshpass -p 'q' ssh -o StrictHostKeyChecking=no root@"+pi+" sudo fallocate -l "+u3+"M "+u1)
#print commands.getoutput(" sshpass -p 'q' ssh -o StrictHostKeyChecking=no root@"+pi+" sudo fallocate -l "+u3+"M "+u1)
#print commands.getoutput(" sshpass -p 'q' ssh -o StrictHostKeyChecking=no root@"+pi+" sudo hadoop fs -Ddfs.replication="+u3+" -Ddfs.block.size="+u4+"  -put "+u1+" "+u2)
print '<div class="container">'
print '<pre><b>'
print commands.getoutput(" sshpass -p 'q' ssh -o StrictHostKeyChecking=no root@" +pi+' sudo hadoop jar /usr/share/hadoop/hadoop-examples-1.2.1.jar wordcount '+u1+' '+u2)
print '</b></pre>'
print '<h1><u><center><span style="color:green">HERE IS THE COUNT </span></u>:-</center></h1>'
print '<pre>'
print '<span style="color:blue">'
print commands.getoutput(" sshpass -p 'q' ssh -o StrictHostKeyChecking=no root@" +pi+' sudo hadoop fs -cat '+u2+'/part-r-00000')
print '</span>'
print '</pre>'
print '<form method="post" action="/p2.html">'
print '<label><input type="submit" value="Click to perform more"></label>'
print '</form>'





