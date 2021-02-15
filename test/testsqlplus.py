#!/usr/bin/env python

import subprocess

database = "dev"
user = "anonymous"
password = user
connectString = user +  "/" + password + "@" + database

def run_sqlplus(script):

	p = subprocess.Popen(['sqlplus','/nolog'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	(stdout,stderr) = p.communicate(script.encode('utf-8'))
	stdout_lines = stdout.decode('utf-8').split("\n")

	return stdout_lines

sqlplus_script = "connect " + connectString + "\n"
sqlplus_script += "set termout off\n"
sqlplus_script += "set head off\n"
sqlplus_script += "set pages 0\n"
sqlplus_script += "set veri off\n"
sqlplus_script += "set feed off\n"
sqlplus_script += "set echo off\n"
sqlplus_script += "set termout on\n"
sqlplus_script += "set linesize 200\n"
sqlplus_script += "SELECT ora_database_name FROM dual;\n"
sqlplus_script += "SELECT object_name FROM user_objects ORDER BY 1;\n"
sqlplus_script += "exit\n"

sqlplus_output = run_sqlplus(sqlplus_script)

for line in sqlplus_output:
	print(line)
