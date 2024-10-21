# import mysql.connector
# from mysql.connector import errors
# import pymysql

# try:
#     conn = pymysql.connect(
#         host="localhost",
#         user="root",
#         password="@Mikist@23.@Mikist@23.",
#         database="employee_data"  # Ensure to provide the correct database name
#     )
#     print("Connection established!")
# except pymysql.MySQLError as err:
#     print(f"Error: {err}")
# finally:
#     if 'conn' in locals() and conn.open:
#         conn.close()

import mysql.connector
import pymysql

# Connect to MySQL server
conn = pymysql.connect(
    host="localhost",
    user="root",
    password="@Mikist@23.@Mikist@23."
)

cursor = conn.cursor()

# Create a new database
cursor.execute("CREATE DATABASE IF NOT EXISTS student_db")
cursor.execute("USE student_db")


# Create a new table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Students(
        StudentID INT AUTO_INCREMENT PRIMARY KEY,
        Name VARCHAR(255) NOT NULL,
        Age INT NOT NULL,
        Major VARCHAR(255) NOT NULL   )
""")



# Insert a new record
def insert_student(name, age, major):
    sql = "INSERT INTO Students (Name, Age, Major) VALUES (%s, %s, %s)"
    val = (name, age, major)
    cursor.execute(sql, val)
    conn.commit()

# 21
# Read all records
def read_students():
    cursor.execute("SELECT * FROM Students")
    result = cursor.fetchall()
    for row in result:
        print(row)

