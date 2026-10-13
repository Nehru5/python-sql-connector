import mysql.connector

# Connectivity
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Nehruraja@12345",
    database="customer_database",
    port="3306"
)
# Checking Connection
if connection.is_connected():
  print("Successfully connected")

# Creating cursor object to execute/write sql queries
cursor = connection.cursor()

cursor.execute("select name,city from users")
data = cursor.fetchall()
print(data)
  
