# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 21:39:57 2017

@author: pnadolny
"""
ip = [''];
username = '';
password = '';

def CassandraConnection(ip, username, password):
    from cassandra.auth import PlainTextAuthProvider
    from cassandra.cluster import ExecutionProfile, EXEC_PROFILE_DEFAULT
    from cassandra.query import tuple_factory
    from dse.cluster import Cluster

    profile = ExecutionProfile(row_factory=tuple_factory)
    auth_provider = PlainTextAuthProvider(username=username, password=password)
    cluster = Cluster(ip, auth_provider=auth_provider, execution_profiles={EXEC_PROFILE_DEFAULT: profile})
    session = cluster.connect()
    query = """select * from... """
    rows = session.execute(query);
    top_row = rows[0];
    print (top_row);
    if top_row.columnName == 'STARTED':
        query = """update where... """;
        session.execute(query);
        print ('Success!')
    else:
        print('Unsuccessful...')
    cluster.shutdown()
