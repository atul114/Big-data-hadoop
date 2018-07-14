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
print yyy
f=open('@ippu','r')
ip=f.read().splitlines()
print  ip

#i=user
#pi=ip[user-1]
pi=ip[0]
print"namenode"
print pi
g=open('/var/www/html/loc','r')
loc=g.read().splitlines()
g.close()
g=open('/var/www/html/locs','r')
locs=g.read().splitlines()
g.close()
ki='192.168.10.102'
print locs
kp=" sudo ssh -o StrictHostKeyChecking=no -i /root/Downloads/2ndjune.pem ec2-user@"+pi+" sudo -i hdfs dfs -Ddfs.replication="+loc[1]+" -Ddfs.block.size="+loc[2]+"  -put /"+locs[0]+" "+loc[3]
print kp
#print commands.getoutput(" sshpass -p 'q' ssh -o StrictHostKeyChecking=no root@" +pi+' sudo hadoop fs -mkdir /sample')
print '<pre>'
print commands.getoutput(" sudo scp -o StrictHostKeyChecking=no -i /root/Downloads/2ndjune.pem "+loc[0]+" ec2-user@"+pi+":/")
print commands.getoutput(" sudo ssh -o StrictHostKeyChecking=no -i /root/Downloads/2ndjune.pem ec2-user@"+pi+"  sudo -i hdfs dfs -Ddfs.replication="+loc[1]+"  -Ddfs.block.size="+loc[2]+"  -put  /"+locs[0]+" "+loc[3])
#print commands.getoutput("sshpass -p 'q' ssh -o StrictHostKeyChecking=no root@"+ki+' sudo hadoop fs -Ddfs.replication='+loc[1]+' -Ddfs.block.size='+loc[2]+' -put '+loc[0]+' '+loc[3])
#print commands.getoutput("sshpass -p 'q' ssh -o StrictHostKeyChecking=no root@"+ki+' sudo hadoop fs -Ddfs.replication='+loc[1]+' -Ddfs.block.size='+loc[2]+' -put '+loc[0]+' '+loc[3])
#print commands.getoutput("sshpass -p 'q' ssh -o StrictHostKeyChecking=no root@"+ki+' sudo hadoop fs -Ddfs.replication='+loc[1]+' -Ddfs.block.size='+loc[2]+' -put '+loc[0]+' '+loc[3])
print '</pre>'
print '<form method="post" action="/cgi-bin/@m6.py">'
print '<label><input type="submit" value="Click to perform more"></label>'
print '</form>'





