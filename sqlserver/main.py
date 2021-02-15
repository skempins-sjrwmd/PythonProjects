import pyodbc
import pandas

# SQL Authentication
conn = pyodbc.connect(
    'Driver={SQL Server};'
    'Server=sqlserverdb;'
    'Database=KofaxDEV2;'
    'UID=anonymous;'
    'PWD=anonymous;')

# open connection
cursor = conn.cursor()

# execute SQL
cursor.execute("SELECT userid, name, description FROM dbo.Users WHERE profileprimarykey <= 20")

# put the results into an object
result = cursor.fetchall()

# get the columns for the result
cols = [column[0] for column in cursor.description]

# iterate over each row and append to list
data = []
for row in result:
    # convert a tuple to a list
    rowlist = list(row)
    data.append(rowlist)

# close connection
cursor.close()

# print the raw result
print("Columns retrieved")
print(cols)
print("Data retrieved")
print(result)

# use pandas to create a formatted output
# create a dataframe
df = pandas.DataFrame(data, columns=cols)

# print the dataframe
print("Output from pandas")
print(df)
