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