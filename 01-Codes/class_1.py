class Emp():
    """This is emp class"""
    e_id = None
    e_name = None
    e_sal = None
    e_dept = None

    def show(self):
        print(self.e_id,self.e_name,self.e_sal,self.e_dept)

obj_1 = Emp()
obj_1.e_id = 101
obj_1.e_name = 'Ram'
obj_1.e_sal = 35000
obj_1.e_dept = 'IT'
obj_1.show()

obj_2 = Emp()
obj_2.e_id = 102
obj_2.e_name = 'Shyam'
obj_2.e_sal = 30000
obj_2.e_dept = 'IT'
obj_2.show()

obj_3 = Emp()
obj_3.e_id = 103
obj_3.e_name = 'Gopal'
obj_3.e_sal = 50000
obj_3.e_dept = 'IT'
obj_3.show()