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
<h2><b><u><span style="color:red">YOUR OPTIONS ARE</u>:-</b></span></h2>
'''
print yyy

f=open('qw','r')
ip=f.read().splitlines()
#print  ip
g=open('nameip','r')
pi=g.read()
g.close()
#print"namenode"
#print pi

print '<pre>'
print commands.getoutput(" sshpass -p 'q' ssh -o StrictHostKeyChecking=no root@" +pi+' sudo wget ftp://192.168.10.102/pub/apache-hive-1.2.1-bin.tar.gz')
print commands.getoutput(" sshpass -p 'q' ssh -o StrictHostKeyChecking=no root@" +pi+' sudo tar -xvzf apache-hive-1.2.1-bin.tar.gz')
print commands.getoutput(" sshpass -p 'q' ssh -o StrictHostKeyChecking=no root@" +pi+' sudo mv apache-hive-1.2.1-bin /hive')
print "-------------------------------------------------SETTING PATH : "+pi+"------------------------------------------------------"
y="# .bashrc\n# User specific aliases and functions\nalias rm='rm -i'\nalias cp='cp -i'\nalias mv='mv -i'\n# Source global definitions\nif [ -f /etc/bashrc ]; then\n	. /etc/bashrc\nfi\nJAVA_HOME=/usr/java/jdk1.7.0_79\nHIVE_PREFIX=/hive\nPATH=$JAVA_HOME/bin:$HIVE_PREFIX/bin:$PATH\nexport PATH"
#y='<?xml version="1.0"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n<!-- Put site-specific property overrides in this file. -->\n<configuration>\n<property>\n<name>dfs.name.dir</name>\n<value>/'+d+'</value>\n</property>\n</configuration>'
f=open('/tmp/.bashrc','w')
f.write(y)
f.close()
commands.getoutput("sshpass -p 'q' sudo scp -o StrictHostKeyChecking=no /tmp/.bashrc root@"+pi+":/root/.bashrc")
print commands.getoutput(" sshpass -p 'q' ssh -o StrictHostKeyChecking=no root@" +pi+' source /root/.bashrc')
print time.sleep(20)
print commands.getoutput(" sshpass -p 'q' ssh -o StrictHostKeyChecking=no root@" +pi+' sudo hadoop fs -chmod 777 /tmp/hive')

print commands.getoutput(" sshpass -p 'q' ssh -o StrictHostKeyChecking=no root@" +pi+' hive')
print time.sleep(20)
print commands.getoutput(" sshpass -p 'q' ssh -o StrictHostKeyChecking=no root@" +pi+' sudo hadoop fs -chmod 777 /tmp/hive')
print time.sleep(20)
print commands.getoutput(" sshpass -p 'q' ssh -o StrictHostKeyChecking=no root@" +pi+' sudo hadoop fs -chmod 777 /tmp/hive')
print commands.getoutput(" sshpass -p 'q' ssh -o StrictHostKeyChecking=no root@" +pi+' hive')
print commands.getoutput(" sshpass -p 'q' ssh -o StrictHostKeyChecking=no root@" +pi+' hive')
print '</pre>'



print '<form method="post" action="/cgi-bin/hivequerystart.py">'
print '<label><input type="submit" value="Click to perform queries"></label>'
print '</form>'































