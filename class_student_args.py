
class Person():

    def __init__(self, data):
        self.trainer = True if data.lower() == "trainer" else False         

    def get_input(self, *args):
        data={
            'designation': 'student' if not self.trainer else 'trainer'
            }
        for row in args:
            data[row] = input("Enter your :%s :"%row)
        return data


data = input("Please enter the record is for Student/Trainer:")
x = Person(data)
persondata = x.get_input('fn','ln', 'email','mobile','address', 'curent_address')
print("Person Data ::", persondata)


