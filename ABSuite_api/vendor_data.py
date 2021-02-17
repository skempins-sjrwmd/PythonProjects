import pyodbc

# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
server = 'absuite' 
database = 'FP' 
username = 'lincinq' 
password = 'win_nt' 

# Select for a sampling of vendors
sql_allvendors = """
SELECT "VENDOR" vndr_cd,
	"VENDNAME1" vndr_nm,
	"ATTN" attn_txt,
	"LOCALE" vndr_tp_cd,
	"MINORITY" mnrty_cd,
	CAST("BANK" as varchar(10)) bnk_no,
	"PAYTYPE" pay_tp,
	"ADDRESS1" addr_1_txt,
	"TEN99" ten99_cd
FROM "BUDGETDB_VENDR"
WHERE "ORG_NBR" = 1
AND "VNSTATUS" = 'A'
AND "VENDOR" like '033%'
"""

# using a bind variable for the vendor code
#sql_onevendor = """
#SELECT "VENDOR" vndr_cd,
#	"VENDNAME1" vndr_nm,
#	"ATTN" attn_txt,
#	"LOCALE" vndr_tp_cd,
#	"MINORITY" mnrty_cd,
#	CAST("BANK" as varchar(10)) bnk_no,
#	"PAYTYPE" pay_tp,
#	"ADDRESS1" addr_1_txt,
#	"TEN99" ten99_cd
#FROM "BUDGETDB_VENDR"
#WHERE "ORG_NBR" = 1
#AND "VNSTATUS" = 'A'
#AND "VENDOR" = ?
#"""
# cursor.execute(sql_allvendors, bindvar) 

def load_db():
	# initialize a dictionary for the data
	return_dataset = []

	# open a connection to the database
	connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

	# create a cursor to execute the query and place all the results in the dictionary
	cursor = connection.cursor()
	cursor.execute(sql_allvendors) 
	for row in cursor:
		return_dataset.append( {"vndr_cd":row[0], "vndr_nm":row[1], "attn_txt":row[2], "vndr_tp_cd":row[3], "mnrty_cd":row[4], "bnk_no":row[5], "pay_tp":row[6], "addr_1_txt":row[7], "ten99_cd":row[8]} )

	# close the connection
	connection.close()
	
	# return the dictionary full of data
	return return_dataset

db = load_db()