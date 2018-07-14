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
<h2></h2>
<p></p>
'''
print yyy
user=1
print user
l=str(user)
d=data.getvalue(l)
#ip=['192.168.10.102','192.168.10.103']
f=open('@ippv','r')
ip=f.read().splitlines()
f.close()
print  ip
f=open('@ippu','r')
ip1=f.read().splitlines()
f.close()
print  ip1

i=user
piu=ip1[user-1]
piv=ip[user-1]
print"namenode"
print piu
print piv
print d
print "<pre>"
print "<center>"
for ik in ip1:
	print '<h3>'
	print '<span style="color:red">'
	print "-------------------SETTING MAPRED_SITE : "+ik+"------------------"
	print '</h3>'
	x='<?xml version="1.0" encoding="UTF-8"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n<!-- Put site-specific property overrides in this file. -->\n<configuration>\n<property>\n<name>mapred.job.tracker</name>\n<value>'+piv+':9001</value>\n</property>\n</configuration>'

	f=open('/tmp/mapred-site.xml','w')
	f.write(x)
	f.close()
	#print commands.getoutput("sshpass -p 'q' ssh -o StrictHostKeyChecking=no root@"+ik+' sudo scp   /tmp/core-site.xml   root@'+ik+':/etc/hadoop/core-site.xml')
	#print commands.getoutput(" sudo ssh -o StrictHostKeyChecking=no -i /root/Downloads/2ndjune.pem ec2-user@"+piu+' sudo -i hadoop namenode  -format')
	print commands.getoutput(" sudo ssh -o StrictHostKeyChecking=no -i /root/Downloads/2ndjune.pem ec2-user@"+piu+' sudo -i mv /hadoop2/etc/hadoop/mapred-site.xml.template /hadoop2/etc/hadoop/mapred-site.xml')
	print commands.getoutput(" sudo scp -o StrictHostKeyChecking=no -i /root/Downloads/2ndjune.pem  /tmp/mapred-site.xml  ec2-user@"+ik+":/hadoop2/etc/hadoop/mapred-site.xml ")
	print '</center>'
	print '</span>'
	print '<span style="color:green">'
	print "<center><h1>SUCCESS!!</h1></center>"
	print '</span>'
	# setting  core-site.xml 
	#print "------------------------------------------SETTING CORE_SITE : "+ik+"-----------------------------------------------------"
	#x='<?xml version="1.0" encoding="UTF-8"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n<!-- Put site-specific property overrides in this file. -->\n<configuration>\n<property>\n<name>fs.defaultFS</name>\n<value>hdfs://'+piv+':10001</value>\n</property>\n</configuration>'

	#f=open('/tmp/core-site.xml','w')
	#f.write(x)
	#f.close()
	#print commands.getoutput(" sudo scp -o StrictHostKeyChecking=no -i /root/Downloads/2ndjune.pem  /tmp/core-site.xml  ec2-user@"+ik+":/hadoop2/etc/hadoop/core-site.xml  ")

print d	
print d
print commands.getoutput(" sudo ssh -o StrictHostKeyChecking=no -i /root/Downloads/2ndjune.pem ec2-user@"+piu+' sudo -i hadoop-daemon.sh start  jobtracker')
print commands.getoutput(" sudo ssh -o StrictHostKeyChecking=no -i /root/Downloads/2ndjune.pem ec2-user@"+piu+' sudo -i jps')


#  setting  up  data  node IPS  

print   "-------------------------------plz wait for a moment  we are making  requirement for data node --------------------------------------"
#time.sleep(2)

dnip=ip1
'''
ll=-1
mn=0
for kk in ip:
	ll=ll+1
	u=ip[ll]
	if(u==pi):
		mn=ll
		break
ip.pop(mn)
print dnip
'''
print  "-----------------------------------------------------setting up  datanode  : -----------------------------------------------------"

#  creating  datanode  hdfs-site.xml
ll=1
print "user"
print user
for j in dnip:
	if(ll==user):
		ll=ll+1
	else:
		dnd=data.getvalue(str(ll))
		print dnd
		#print "SETTING HDFS_SITE : "+j
		#z='<?xml version="1.0" encoding="UTF-8"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n<!-- Put site-specific property overrides in thisfile. -->\n<configuration>\n<property>\n<name>dfs.datanode.data.dir</name>\n<value>/'+dnd+'</value>\n</property>\n</configuration>'
		#f=open('/tmp/hdfsdn-site.xml','w')
		#f.write(z)
		#f.close()
		#print commands.getoutput(" sudo scp -o StrictHostKeyChecking=no -i /root/Downloads/2ndjune.pem /tmp/hdfsdn-site.xml ec2-user@"+j+":/hadoop2/etc/hadoop/hdfs-site.xml")
		print commands.getoutput(" sudo ssh -o StrictHostKeyChecking=no -i /root/Downloads/2ndjune.pem ec2-user@"+j+' sudo -i hadoop-daemon.sh start tasktracker')
		print commands.getoutput(" sudo ssh -o StrictHostKeyChecking=no -i /root/Downloads/2ndjune.pem ec2-user@"+j+' sudo -i jps')
		ll=ll+1

print '</pre>'
print '<h2>SETUP SUCCESSFUL!!</h2>'
print '<form method="post" action="/cgi-bin/@mapindex.py.py">'
print '<div>'
print '<label><input type="submit" value="Click to start processing "></label>'
print '</div>'
print "<input type ='hidden' name='p' value="+str(user)+">"
print '</form>'













