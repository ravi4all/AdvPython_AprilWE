class User():

    def __init__(self, name, email, pwd, city):
        self.name = name
        self.email = email
        self.pwd = pwd
        self.city = city

    def __str__(self):
        return self.name + "," + self.email + "," + self.pwd + "," + self.city

users = []
def addUser(name, email, pwd, city):
    # print(name, email, pwd, city)
    user = User(name, email, pwd, city)
    users.append(user)
    return user

def searchUser(email):
    for user in users:
        userList = str(user).split(",")
        if email in userList:
            # print(userList)
            return userList
    else:
        # print("User Not Found")
        return "User Not Found"
