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
<h2></h2>
<p></p>
'''
print yyy

#ip=['192.168.10.102','192.168.10.103']
g=open('nameip','r')
pi=g.read()
g.close()
f=open('qw','r')
ip=f.read().splitlines()
#print  ip
#print"namenode"
#print pi
print "<pre>"

for ik in ip:
	# setting  mapred-site.xml 
	print "<center>"
	print '<h3>'
	print '<span style="color:red">'
	print "-------------------SETTING MAPRED_SITE : "+ik+"------------------"
	print '</h3>'
	x='<?xml version="1.0"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n<!-- Put site-specific property overrides in this file. -->\n<configuration>\n<property>\n<name>mapred.job.tracker</name>\n<value>'+pi+':9001</value>\n</property>\n</configuration>'

	f=open('/tmp/mapred-site.xml','w')
	f.write(x)
	f.close()
	#print commands.getoutput("sshpass -p 'q' ssh -o StrictHostKeyChecking=no root@"+ik+' sudo scp   /tmp/core-site.xml   root@'+ik+':/etc/hadoop/core-site.xml')
	commands.getoutput(" sshpass -p 'q' sudo scp -o StrictHostKeyChecking=no /tmp/mapred-site.xml  root@"+ik+":/etc/hadoop/mapred-site.xml ")
	print '</center>'
	print '</span>'
	print '<span style="color:green">'
	print "<center><h1>SUCCESS!!</h1></center>"
	print '</span>'

print "<center>"
print '<h3>'
print '<span style="color:blue">'
print commands.getoutput("sshpass -p 'q' ssh -o StrictHostKeyChecking=no root@"+pi+' sudo hadoop-daemon.sh start jobtracker')
print commands.getoutput("sshpass -p 'q' ssh -o StrictHostKeyChecking=no root@"+pi+' sudo jps')
print '</h3>'
print '</center>'
print '</span>'

dnip=ip
ll=1
for j in dnip:
	if(j==pi):
		ll=ll+1
	else:
		print "<center>"
		print '<h3>'
		print '<span style="color:blue">'
		print commands.getoutput("sshpass -p 'q' ssh -o StrictHostKeyChecking=no root@"+j+' sudo hadoop-daemon.sh start tasktracker')
		print commands.getoutput("sshpass -p 'q' ssh -o StrictHostKeyChecking=no root@"+j+' sudo jps')
		print '</h3>'
		print '</center>'
		print '</span>'
		ll=ll+1


print '</pre>'
print '<h2>WHOLE SETUP SUCCESSFUL!!</h2>'
print '<form method="post" action="/p2.html">'
print '<div>'
print '<label><input type="submit" value="Click to start prcessing "></label>'
print '</div>'
print '</form>'




