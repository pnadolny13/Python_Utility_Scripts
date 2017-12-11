# -*- coding: utf-8 -*-
"""
Created on Wed May 31 15:54:52 2017

@author: pnadolny
"""
username = 'username' 
password = 'password'
Server1 = 'ip address 1';
Server2 = 'ip address 2' ;
AllServers = [Server1, Server2];

import paramiko

nbytes = 4096
port = 22
command = 'cd bin n\ runscript.sh'
for ip in AllServers:
    hostname = ip;
    client = paramiko.Transport((hostname, port))
    client.connect(username=username, password=password)
    stdout_data = []
    stderr_data = []
    session = client.open_channel(kind='session')
    session.exec_command(command)
    while True:
        if session.recv_ready():
            stdout_data.append(session.recv(nbytes))
        if session.recv_stderr_ready():
            stderr_data.append(session.recv_stderr(nbytes))
        if session.exit_status_ready():
            break
    print ('exit status: ', session.recv_exit_status())
    print (stdout_data)
    print (stderr_data)
    session.close()
    client.close()











#Dev:
#Index1 ='';
Index2 = 'ip address 1';
Search1 = 'ip address 2' ;
AllServers = [Index2, Search1];

import datetime
date = (str(datetime.datetime.now())[:10]);
       
##################DEV INDEX2 Connection - kill all
import paramiko
import sys

nbytes = 4096
#hostname = '10.64.68.106'
port = 22
username = 'T11' 
password = 'T11'
command = 'cd bin n\ kill_Q.sh ' #n\ kill_D.sh n\ snapshotQ.sh n\ snapshotD.sh PGPat n\ snapshotD.sh PGPub'
for ip in AllServers:
    hostname = ip;
    client = paramiko.Transport((hostname, port))
    client.connect(username=username, password=password)
    stdout_data = []
    stderr_data = []
    session = client.open_channel(kind='session')
    session.exec_command(command)
    while True:
        if session.recv_ready():
            stdout_data.append(session.recv(nbytes))
        if session.recv_stderr_ready():
            stderr_data.append(session.recv_stderr(nbytes))
        if session.exit_status_ready():
            break
    print ('exit status: ', session.recv_exit_status())
    print (stdout_data)
    print (stderr_data)
    session.close()
    client.close()


####################DEV INDEX1 Connection - kill all
import paramiko
import sys

nbytes = 4096
hostname = ''
port = 22
username = 'T11' 
password = 'T11'
command = 'cd bin n\ kill_Q.sh n\ kill_D.sh n\ snapshotQ.sh n\ snapshotD.sh PGPat n\ snapshotD.sh PGPub'

client = paramiko.Transport((hostname, port))
client.connect(username=username, password=password)

stdout_data = []
stderr_data = []
session = client.open_channel(kind='session')
session.exec_command(command)
while True:
    if session.recv_ready():
        stdout_data.append(session.recv(nbytes))
    if session.recv_stderr_ready():
        stderr_data.append(session.recv_stderr(nbytes))
    if session.exit_status_ready():
        break

print ('exit status: ', session.recv_exit_status())
print (stdout_data)
print (stderr_data)

session.close()
client.close()


####################DEV Search 1 Connection - kill all
import paramiko
import sys

nbytes = 4096
hostname = '10.64.68.67'
port = 22
username = 'T11' 
password = 'T11'
command = 'cd bin n\ kill_Q.sh n\ kill_D.sh n\ snapshotQ.sh n\ snapshotD.sh PGPat n\ snapshotD.sh PGPub'

client = paramiko.Transport((hostname, port))
client.connect(username=username, password=password)

stdout_data = []
stderr_data = []
session = client.open_channel(kind='session')
session.exec_command(command)
while True:
    if session.recv_ready():
        stdout_data.append(session.recv(nbytes))
    if session.recv_stderr_ready():
        stderr_data.append(session.recv_stderr(nbytes))
    if session.exit_status_ready():
        break

print ('exit status: ', session.recv_exit_status())
print (stdout_data)
print (stderr_data)

session.close()
client.close()




















import datetime
date = (str(datetime.datetime.now())[:10]);

##### Clean and Restart - index 2

import paramiko
import sys

nbytes = 4096
hostname = '10.64.68.106'
port = 22
username = 'T11' 
password = 'T11'
#command = 'cd bin ; cd AllServicesNohup ; touch test'
command = 'cd bin ; cd AllServicesNohup ; mv nohup.out nohup.out_' + date + ' ; cd ../ ; cd PatiPostNohup ; mv nohup.out nohup.out_' + date + ' ; rm -r /PAPES_DEV/PatiApps/* ; rm -r /PAPES_DEV/AIP_EXT_INTERFACE_T11/TempForCsvProcessing/*'

client = paramiko.Transport((hostname, port))
client.connect(username=username, password=password)

stdout_data = []
stderr_data = []
session = client.open_channel(kind='session')
session.exec_command(command)
while True:
    if session.recv_ready():
        stdout_data.append(session.recv(nbytes))
    if session.recv_stderr_ready():
        stderr_data.append(session.recv_stderr(nbytes))
    if session.exit_status_ready():
        break

print ('exit status: ', session.recv_exit_status())
print (stdout_data)
print (stderr_data)

session.close()
client.close()





















### Restart Services 
server = 'Index1'
import paramiko
import sys

nbytes = 4096
hostname = Index1
port = 22
username = 'T11' 
password = 'T11'
command = 'cd bin/AllServicesNohup/ \n startAllServices.sh \n startAllWorkers_' + server +'.sh'

client = paramiko.Transport((hostname, port))
client.connect(username=username, password=password)

stdout_data = []
stderr_data = []
session = client.open_channel(kind='session')
session.exec_command(command)
while True:
    if session.recv_ready():
        stdout_data.append(session.recv(nbytes))
    if session.recv_stderr_ready():
        stderr_data.append(session.recv_stderr(nbytes))
    if session.exit_status_ready():
        break

print ('exit status: ', session.recv_exit_status())
print (stdout_data)
print (stderr_data)

session.close()
client.close()



############################################
server = 'Index2'
import paramiko
import sys

nbytes = 4096
hostname = Index2
port = 22
username = 'T11' 
password = 'T11'
command = 'cd bin/AllServicesNohup/ \n startAllServices.sh \n startAllWorkers_' + server +'.sh'

client = paramiko.Transport((hostname, port))
client.connect(username=username, password=password)

stdout_data = []
stderr_data = []
session = client.open_channel(kind='session')
session.exec_command(command)
while True:
    if session.recv_ready():
        stdout_data.append(session.recv(nbytes))
    if session.recv_stderr_ready():
        stderr_data.append(session.recv_stderr(nbytes))
    if session.exit_status_ready():
        break

print ('exit status: ', session.recv_exit_status())
print (stdout_data)
print (stderr_data)

session.close()
client.close()


#############################################################
server = 'Search1'
import paramiko
import sys

nbytes = 4096
hostname = Search1
port = 22
username = 'T11' 
password = 'T11'
command = 'cd bin/AllServicesNohup/ \n startAllServices.sh \n startAllWorkers_' + server +'.sh'

client = paramiko.Transport((hostname, port))
client.connect(username=username, password=password)

stdout_data = []
stderr_data = []
session = client.open_channel(kind='session')
session.exec_command(command)
while True:
    if session.recv_ready():
        stdout_data.append(session.recv(nbytes))
    if session.recv_stderr_ready():
        stderr_data.append(session.recv_stderr(nbytes))
    if session.exit_status_ready():
        break

print ('exit status: ', session.recv_exit_status())
print (stdout_data)
print (stderr_data)

session.close()
client.close()



























#Index/Search (killQ, killD, snapshotQ, snapshotD PGPat, snapshotD PGPub) on each server
#bin: PatiPost (move nohup and clean), AllServices (move nohup and clean)
# clean AIP_EX: clean PatiApps, clean TempForCSV, clean INPUTQ and D
# query Cassandra for batch numbers of PATI and POST, then use batch number to set current batch to 'failed' if it is 'Started'
# restart everything, startallServices, startallworkers index1, index2, search1, PatiPost



