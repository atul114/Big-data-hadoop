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
pi='172.17.0.2'
print '<b>'
hhh='''
<form method="post" action="/cgi-bin/dockercheck5.py">
<div class="radio">
      <label><input type="radio" name="op" value='1'><b>Select for making and uploading a sample directory</b> (just makes a directory of name 'sample' in /)</label>
    </div>
<div class="radio">
      <label><input type="radio" name="op" value='18'><b>Select for making and uploading a sample directory</b> (just makes a directory of name 'sample' in other location of your choice )</label>
    </div>
<div class="radio">
      <label><input type="radio" name="op" value='2'><b>Select for making and uploading a sample file</b> (make a file of desired size and upload it in the cluster with desired replication factor and block size) </label>
    </div>
<div class="radio">
      <label><input type="radio" name="op" value='3'><b>Select for uploading an existing file from your own computer </b>(uploads an existing file to the cluster )</label>
    </div>
<div class="radio">
      <label><input type="radio" name="op" value='4'><b>Select for going in safe mode </b></label>
    </div>
<div class="radio">
      <label><input type="radio" name="op" value='5'><b>Select for setting user Quota</b></label>
    </div>
<div class="radio">
      <label><input type="radio" name="op" value='6'><b>Select for setting space Quota</b></label>
    </div>
<div class="radio">
      <label><input type="radio" name="op" value='7'><b>Select for clearing user Quota</b></label>
    </div>
<div class="radio">
      <label><input type="radio" name="op" value='8'><b>Select for clearing space Quota</b></label>
    </div>
<div class="radio">
      <label><input type="radio" name="op" value='9'><b>Select for seeing the Quota that is set</b></label>
    </div>
<div class="radio">
      <label><input type="radio" name="op" value='10'><b>Select for seeing the uplaoded directories and files</b></label>
    </div>
<div class="radio">
      <label><input type="radio" name="op" value='11'>Select to permanently set the replication and block size</label>
    </div>
<div class="radio">
      <label><input type="radio" name="op" value='12'>Select to change the replication and block to the default values</label>
    </div>
<div class="radio">
      <label><input type="radio" name="op" value='13'>Select to upload with different replication and block size</label>
    </div>
<div class="radio">
      <label><input type="radio" name="op" value='14'>Select to upload</label>
    </div>
<div class="radio">
      <label><input type="radio" name="op" value='15'><b>Select to leave safe mode</b></label>
    </div>
<div class="radio">
      <label><input type="radio" name="op" value='0'>Select to exit</label>
    </div>
<div class="radio">
      <label><input type="radio" name="op" value='16'><b>Select to see total space</b></label>
    </div>
<div class="radio">
      <label><input type="radio" name="op" value='17'><b>UPLOAD</b></label>
    </div>
'''
print hhh
print '<label><input type="submit" value="Click to perform"></label>'
#print "<input type ='hidden' name='p' value="+str(user)+">"
print '</form>'
print '</b>'
print '</body>'
