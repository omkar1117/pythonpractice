
class Person():

    def get_input(self, *args):
        desg = 'trainer'
        if self.student:
            desg = 'student'
            
        data={'designation': desg}
        print("Arguments Here::", args[0])
        
        for row in args[0]:
            data[row] = input("Enter your :%s :"%row)
        return data


class Student(Person):

    def __init__(self):
        self.student = True

    def field_names(self):
        return 'fn', 'ln', 'email','mobile','address', 'curent_address'



class Trainer(Person):

    def __init__(self):
        self.student = False

    def field_names(self):
        return 'fn', 'ln', 'email','mobile','address', 'curent_address', 'exp'


x = Student()
x.get_input(x.field_names())

y=Trainer()
y.get_input(y.field_names())

    
