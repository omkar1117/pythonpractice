import datetime

def validate_names(fn, ln, mn=None):
    data = "First and Last names entered"
    if mn:
        data = "The User have First, Last and Middle Names"
    return fn,ln, mn, data


fn = input("Enter the First Name:")
ln = input("Enter the Last Name:")
mn = input("Enter the Middle Name:")

(fn, ln, mn, data) = validate_names(fn,ln=ln, mn=mn)

x = datetime.datetime.now()
y = x.strftime("%d_%m_%Y_%H_%M_%S")
log_file_name = "student_details_%s.log" %y

fp = open(log_file_name, "a")
fp.write("-----------------------\n")
fp.write(data)
fp.close()

