import sys
# add the tools directory to the path so getpassword can be imported
sys.path.append(r"C:\_SourceControl\server-tools\bin")
import getpassword

mypassword_file = r"C:\TEMP\mypassword.txt"

mypassword = getpassword.lookupDBPassword(passwordfile=mypassword_file, database="dev", username="ingres")

if mypassword != None:
	print(mypassword)
else:
	print("password not found")