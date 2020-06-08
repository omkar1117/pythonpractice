fname = input("Enter your First name:")
lname = input("Enter your Last name:")
email = input("Enter your Email:")

if not fname and not lname and not email:
    print("Please enter all the details:")

elif fname and lname and not email:
    print("Please enter a valid email")

elif email and fname and not lname:
    print("First Name and Last name both are mandatory")

elif email and lname and not fname:
    print("First Name and Last name both are mandatory")

if email and not '@' in email:
    print("Not a valid Email, Please have a valid email")

elif fname.strip() and lname.strip() and email.strip():
    fw = open("details.txt", "a")
    fw.write("-------------------------------------------\n")
    fw.write("First Name is  ::  %s \n"%fname.capitalize())
    fw.write("Last Name is   ::  %s \n"%lname.capitalize())
    fw.write("Email is       ::  %s \n"%email.lower())
    fw.write("-------------------------------------------\n")
    fw.close()
print("End of Script completed")
