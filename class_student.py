
class Person():

    def get_input(self, trainer=False, student=False):
        fn = input("Enter your First name:")
        ln = input("Enter your Last name:")
        
        if trainer:
            exp = input("Enter your Previous experience")
            previous_history = input("Previous work history")
        address = input("Enter the Address:")

        if student:
            parent_name = input("Enter your parent details:")

x = Person()
data = input("Please enter the record is for Student/Trainer")
student = True if data.lower() == "student" else False
trainer = False if student else True
x.get_input(student=student, trainer=trainer)


