import mysql.connector

connection = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Nehruraja@12345",
  database="customer_database",
  port="3306"
)
if connection.is_connected():
  print("Connected successfully......")
  
name = input("Enter your name: ")
age = int(input("Enter Age: "))
city = input("Enter City:")
  
cursor = connection.cursor()
query = "insert into users(name,age,city) values(%s,%s,%s)"
data =(name,age,city)
cursor.execute(query,data)
connection.commit()
print("Data saved successfully...")
