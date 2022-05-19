import pyodbc

try:
    connection = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ='
                                r'C:\Users\RHONAN\Documents\Database1.accdb;')
    print("Database is Connected")

except pyodbc.Error:
    print("Database is NOT connected")
