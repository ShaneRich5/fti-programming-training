import pypyodbc

# Define connection string
connection_string = 'Driver={SQL Server Native Client 11.0};Server=YOURSERVER;'
'Database=YOURDATABASE;Uid=YOURUSERID;Pwd=YOURPASSWORD;'

# Open the connection
connection = pypyodbc.connect(connection_string)

# Define query
SQL = "YOUR SQL QUERY HERE"

# Execute query
cur = connection.cursor()
cur.execute(SQL)

# Print the result. Hint:
#     cur.description
#         This read-only property returns a list of tuples describing the columns
#         in a result set.
#     cur.fetchall():
#         The method fetches all (or all remaining) rows of a query result set
#         and returns a list of tuples. If no more rows are available, it returns
#         an empty list.

# Close the connection
cur.close()
connection.close()