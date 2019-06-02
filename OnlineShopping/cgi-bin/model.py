import pymysql
import os

connection = pymysql.connect(host='localhost', user='root', port=3306, database='onlineshopping', autocommit=True)

cursor = connection.cursor()

class User():

    def __init__(self, name, email, pwd, phno, pic):
        self.name = name
        self.email = email
        self.pwd = pwd
        self.phno = phno
        self.pic = pic

def registerUser(name,email,pwd,phno,image):
    if image.filename:
        print("Filename is",image.filename)
        fn = os.path.basename(image.filename)
        open("images/"+fn, 'wb').write(image.file.read())
        # print("Image saved...",fn)

    query = "INSERT INTO users VALUES (%S,%s,%s,%s,%s)"
    obj = User(name,email,pwd,phno,image)
    values = (obj.name,obj.email,obj.pwd,obj.phno,obj.pic)
    cursor.execute(query, values)

def loginUser(email,pwd):
    pass
