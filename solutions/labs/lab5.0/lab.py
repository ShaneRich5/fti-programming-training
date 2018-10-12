import pypyodbc
import getpass

# Ask user for connection details
server = input('Server: ')
database = input('Database: ')
userid = input('Username: ')
password = getpass.getpass()
table = input('Table: ')

# Format connection string
connection_string_template = 'Driver={{SQL Server Native Client 11.0}};Server={};Database={};Uid={};Pwd={};'
connection_string = connection_string_template.format(server, database, userid, password)

# Connect
connection = pypyodbc.connect(connection_string)

# Define query
SQL = 'SELECT TOP 100 * FROM ' + table

# Execute query
cur = connection.cursor()
cur.execute(SQL)

# Print the result
for d in cur.description:
    print (d[0], end=" ")
print('')
for row in cur.fetchall():
    for field in row:
        print (field, end=" ")
    print ('')

# Close the connection
cur.close()
connection.close()