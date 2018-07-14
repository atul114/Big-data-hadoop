#!/usr/bin python2
import socket,time,os,commands

#create the socket
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#take the drive name and drive size as input from the client
drive_name = raw_input("Enter required drive name:-")
drive_size = raw_input("Enter required drive size:-")
server_ip = "192.168.1.100"

#send the drive data to the server
s.sendto(drivename,(server_ip,8888)
s.sendto(drivesize,(server_ip,8888)

#recieve the respond messgae from the server
reply = s.recvfrom(1000)

#just a debugging process
print "You got a reply:-" + reply

#chek for software availability and start the service
commands.getoutput("yum install rpcbind -y")
commands.getoutput("systemctl start rpcbind")

#make the direcoty in for mounting
commands.getoutput("mkdir /media/" + drive_name")

mount_point = "/media/" + drive_name

#check for the valid reply
if "ok" in reply:
	#just a debugging process
	shared_drives = commands.getoutput("showmount -e" + " " + server_ip)
	print "The drive that are shared for you by the drive are" + " " + shared_drives

	#mount the server shared directory to your mount point
	print commands.getoutput("mount -t nfs" + " " + server_ip + ":/mnt/" + drive_name + " " + mount_point)
	print "ALL DONE YOU HAVE GOT YOUR REQUIRED DRIVE")



