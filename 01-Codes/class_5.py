class Emp():

    # Constructor
    def __init__(self):
        self.empRecord = []
        self.e_id = None
        self.e_name = None
        self.e_sal = None
        self.e_dept = None

    def show(self):
        self.empRecord.append([self.e_id, self.e_name, self.e_sal, self.e_dept])
        # print(self.empRecord)

    # tostring - convert object to readable format
    def __str__(self):
        return str(self.empRecord)

obj_1 = Emp()
obj_1.e_id = 101
obj_1.e_name = 'Ram'
obj_1.e_sal = 35000
obj_1.e_dept = 'IT'
obj_1.show()
print(obj_1)

obj_2 = Emp()
obj_2.e_id = 102
obj_2.e_name = 'Shyam'
obj_2.e_sal = 30000
obj_2.e_dept = 'IT'
obj_2.show()
print(obj_2)