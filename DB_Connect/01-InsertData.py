import pymysql

connection = pymysql.connect(host='localhost', port=3306,
                             database = 'pythonMorning', user='root',
                             autocommit = True)

cursor = connection.cursor()
# query = "INSERT INTO users VALUES ('Ram', 'ram@gmail.com', '1234', 'delhi')"

name = 'Shyam'
email = 'shyam@gmail.com'
pwd = 'shyam12'
city = 'pune'

query = "INSERT INTO users VALUES (%s, %s, %s, %s)"
cursor.execute(query, (name, email, pwd, city))
print("Data Inserted Successfully...")