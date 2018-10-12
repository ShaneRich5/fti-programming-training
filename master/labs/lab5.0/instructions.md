# Objective: Connect to a remote SQL Server database and execute a query.
**The connection details are to be provided by the instructor.**
1. Use the pypyodbc module to make the connection.
2. Ask the user for the connection details and store them in variables, but ensure the password is received securely and kept hidden from the script output.
3. Use the format() method to inject the credentials into the connection string.
4. Select the first 100 rows of the table and output the values of each record.