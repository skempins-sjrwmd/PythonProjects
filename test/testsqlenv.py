#!/usr/bin/env python

from subprocess import Popen, PIPE

database = "dev"
user = "anonymous"
password = user
connectString = user +  "/" + password + "@" + database

def runSQLQuery(sqlCommand, connectString):
	#session = Popen(['sqlplus', '-S', connectString], stdin=PIPE, stdout=PIPE, stderr=PIPE)
	session = Popen("/bin/bash",  stdin=PIPE, stdout=PIPE, stderr=PIPE)
	session.stdin.write("ORACLE_HOME=/opt/oracle/product/12.1.0.2; export ORACLE_HOME")
	session.stdin.write("ORACLE_BASE=/opt/oracle; export ORACLE_BASE")
	session.stdin.write("ORACLE_TOOLS=$ORACLE_BASE/tools; export ORACLE_TOOLS")
	session.stdin.write("PATH=$ORACLE_HOME/bin:$ORACLE_TOOLS/bin:$PATH")
	session.stdin.write("LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$ORACLE_HOME/lib")

	session.stdin.write("sqlplus -S "+ connectString)
#	session.stdin.write(sqlCommand)
	return session.communicate()

sqlstmt = "SELECT ora_database_name FROM dual;"
sqlstmt = sqlstmt + "\n" + "SELECT count(*) FROM user_tables;"
#sqlstmt = "select a from b;"

queryResult, errorMessage = runSQLQuery(sqlstmt, connectString)

print("Result is:")
print(queryResult)
print("Error is:")
print(errorMessage)
