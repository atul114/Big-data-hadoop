#!/usr/bin/python

import  cgi
import time
import commands
import os
import collections



f=open('ips','w')
f.write( commands.getoutput('aws ec2 describe-instances | grep PublicIpAddress | grep -o -P "\d+\.\d+\.\d+\.\d+" | grep -v "^10\."'))
f.close()




















