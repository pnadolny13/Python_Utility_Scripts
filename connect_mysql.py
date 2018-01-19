# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 21:46:40 2018

@author: pnadolny
"""
import pymysql
hostname  = ""
username = ""
password = ""
database = ""

myConnection = pymysql.connect( host=hostname, user=username, passwd=password, db=database )
runSQL( myConnection )
myConnection.close()

def runSQL( conn ) :
    cur = conn.cursor()
    cur.execute( "insert into test_db (col1, col2) values ( 'test1', 'test2');" )
    conn.commit()