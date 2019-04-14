import sys
sys.path.append('..')

from controller import controller

def addUser():
    name = input("Enter your name : ")
    email = input("Enter your email : ")
    pwd = input("Enter your password : ")
    city = input("Enter your city : ")
    user = controller.addUser(name, email, pwd, city)
    print(str(user).split(","))

def deleteUser():
    pass

def readUser():
    pass

def searchUser():
    email = input("Enter Email : ")
    data = controller.searchUser(email)
    print(data)

while True:
    print("""
    1. Add
    2. Read
    3. Update
    4. Delete
    5. Search
    6. Sort
    """)

    ch = input("Enter your choice : ")
    todo = {
        "1" : addUser,
        "2" : readUser,
        "4" : deleteUser,
        "5" : searchUser
    }
    todo.get(ch)()
