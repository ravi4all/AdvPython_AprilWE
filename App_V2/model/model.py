import pymysql

class User():

    def __init__(self, name, email, pwd, city):
        self.name = name
        self.email = email
        self.pwd = pwd
        self.city = city

    def __str__(self):
        return self.name + "," + self.email + "," + self.pwd + "," + self.city

connection = pymysql.connect(host='localhost', port=3306,
                             database = 'pythonMorning', user='root',
                             autocommit = True)

cursor = connection.cursor()

def addUser(name, email, pwd, city):
    # print(name, email, pwd, city)
    user = User(name, email, pwd, city)
    query = "INSERT INTO users VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (name, email, pwd, city))
    return user

def searchUser(email):
    pass
