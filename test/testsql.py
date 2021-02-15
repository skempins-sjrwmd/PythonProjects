#!/usr/bin/env python

from subprocess import Popen, PIPE

database = "dev"
user = "anonymous"
password = user
connectString = user +  "/" + password + "@" + database

def runSQLQuery(sqlCommand, connectString):
	session = Popen(['sqlplus', '-S', connectString], stdin=PIPE, stdout=PIPE, stderr=PIPE)
	session.stdin.write(sqlCommand)
	return session.communicate()

sqlstmt = "set termout off\nset head off\nset pages 0\nset veri off\nset feed off\nset echo off\nset termout on\nset linesize 200"
sqlstmt = sqlstmt + "\nSELECT ora_database_name FROM dual;"
sqlstmt = sqlstmt + "\nSELECT count(*) FROM user_tables;"
#sqlstmt = "select a from b;"

queryResult, errorMessage = runSQLQuery(sqlstmt, connectString)

print("Result is:")
print(queryResult)
print("Error is:")
print(errorMessage)
