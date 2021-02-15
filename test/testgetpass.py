#!/usr/bin/python
import subprocess

#connectString="sjr/sjr@wht"
#tmpdir="/tmp"

#loadcmd = '/opt/oracle/product/12.1.0.2/bin/sqlldr '+connectString+' CONTROL='+tmpdir+'/loadunitlog.ctl'+' BAD='+tmpdir+'/loadunitlog.bad'+' LOG='+tmpdir+'/loadunitlog.log'+' ERRORS=100000'
#loadcmd = 'ls /tmp'
#print(loadcmd)
#session = subprocess.Popen(loadcmd.split(' '))
#session_output = session.communicate()


ORACLE_SID = "wht"
username = "sjr"

cmd = "getpassword " + ORACLE_SID + " " + username
print(cmd)
session = subprocess.Popen(cmd.split(" "), stdout=subprocess.PIPE)
password, errors = session.communicate()
print("password is "+password)
