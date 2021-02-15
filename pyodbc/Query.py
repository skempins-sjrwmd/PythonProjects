import pyodbc

# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
server = 'absuite' 
database = 'FP' 
username = 'lincinq' 
password = 'win_nt' 

# Select for a sampling of vendors
sql = """
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
AND "VENDOR" like '0333%'
"""

connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

#Sample select query
cursor = connection.cursor()
cursor.execute(sql) 

print(cursor.fetchall())

#for row in cursor:
#	print(row)

cursor.close()
connection.close()