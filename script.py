import pyodbc
import pandas as pd
import os
from datetime import datetime
# from plyer import notification

# create SQL connection
server = 'NUKROB-NT\SQLEXPRESS' 
database = 'RecordNewDB' 
username = 'sa' 
password = ''
driver = '{ODBC Driver 13 for SQL Server}' 
connection = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
                           
# SQL Command to read the data
sqlQuery = "select UserDB.dbo.Users.UserName,RecordNewDB.dbo.Record.StartTimeLocal, RecordNewDB.dbo.Record.StopTimeLocal, format(RecordNewDB.dbo.Record.Duration, '00:00:00') As Duration,RecordNewDB.dbo.Record.CallerID,RecordNewDB.dbo.Record.CalledID,(CASE RecordNewDB.dbo.Record.Direction WHEN '1' THEN 'CALL IN' WHEN '2' THEN 'CALL OUT' END) As Direction from RecordNewDB.dbo.Record inner join UserDB.dbo.Users on RecordNewDB.dbo.Record.UserID = UserDB.dbo.Users.UserId where RecordNewDB.dbo.Record.Duration >= '10'"

# Getting the data from sql into pandas dataframe
df = pd.read_sql(sql = sqlQuery, con = connection)

# Export the data on the Desktop
directory = '\\\\NUKROB-NT\\Report\\'
df.to_excel(directory + "SQL_ReportData_" +
 datetime.now().strftime("%d-%b-%Y %H%M%S")
         + ".xlsx", index = False)

# Display Notifiction to User
# notification.notify(title="Report Status!!!",
#                    message=f"Report data has been successfully saved into Excel.\
#                    \nTotal Rows: {df.shape[0]}\nTotal Columns: {df.shape[1]}",
#                    timeout = 10)
