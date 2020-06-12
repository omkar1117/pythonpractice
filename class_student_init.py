
class Person():

    def __init__(self, data):
        self.trainer = True if data.lower() == "trainer" else False         

    def get_input(self):
        fn = input("Enter your First name:")
        ln = input("Enter your Last name:")
        
        if self.trainer:
            exp = input("Enter your Previous experience:")
            previous_history = input("Previous work history:")
        else:
            parent_name = input("Enter your parent details:")
            
        address = input("Enter the Address:")

data = input("Please enter the record is for Student/Trainer:")
x = Person(data)
x.get_input()


