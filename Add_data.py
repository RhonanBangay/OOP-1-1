import pyodbc

try:
    conn = r'Driver={Microsoft Access Driver (*.mdb, *.accdb)}; DBQ=C:\Users\RHONAN\Documents\Database1.accdb;'
    connection = pyodbc.connect(conn)

    database = connection.cursor()

    add_user = (10, "Rhonan Richmond D. Bangay",20, 'BSCPE',91, 'Cavite')

    database.execute('INSERT INTO Table1 VALUES (?,?,?,?,?,?)', add_user)

    connection.commit()
    print("Database Inserted")


except pyodbc.Error:
    print("Inserting data failed")