import pymysql

connection = pymysql.connect(host='localhost', port=3306,
                             database = 'pythonMorning', user='root',
                             autocommit = True)

cursor = connection.cursor()
email = 'ram@gmail.com'
pwd = '1234'
# query = "SELECT * FROM users"
query = "SELECT * FROM users WHERE email = %s AND pwd = %s"
cursor.execute(query, (email, pwd))
print(cursor.rowcount)
data = cursor.fetchall()
print(data)
