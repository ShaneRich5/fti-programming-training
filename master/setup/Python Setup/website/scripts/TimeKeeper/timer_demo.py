"""
Record project information and elapsed time to an Excel time sheet.
"""

import os  # Handles paths
import time as t  # Record time
import openpyxl as xl  # Interface with Excel

from datetime import datetime as dt  # Get today's date and format it


# Record user input
project = input("What is the name of your project?\n")
matter_id = input("What is the Matter ID?\n")
description = input("Type your narrative here:\n")
date = dt.today().strftime('%m/%d/%Y')  # Get and format date

stop = None  # Helper variable to control the while loop
tic = t.time()  # Start keeping the time
while stop is None:
    stop = input("Press any key to stop...")  # Prompt user while condition holds
    if stop is not None:  # Condition no longer True when user presses a key
        toc = t.time()  # Store the time and calculate the difference
        elapsed_time = round(toc - tic, 2)
        print("{0:.2f}hrs Elapsed...".format(elapsed_time))
        break  # Exit the loop!

root = os.getcwd()
timesheet = os.path.join(root, 'timesheet.xlsx')  # Point to the time sheet
# Store the data as a list data structure
row = [str(date), project, str(matter_id), str(elapsed_time), description]
wb = xl.load_workbook(timesheet)  # Load the time sheet
ws = wb.get_active_sheet()  # Tell Python to work with the active sheet
ws.append(row)  # Append the row to the time sheet
wb.save(timesheet)  # Save these changes
