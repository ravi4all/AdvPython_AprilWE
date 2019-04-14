import sys
sys.path.append('..')
from model import model

def addUser(name, email, pwd, city):
    user = model.addUser(name, email, pwd, city)
    return user

def deleteUser():
    pass

def searchUser(email):
    data = model.searchUser(email)
    return data