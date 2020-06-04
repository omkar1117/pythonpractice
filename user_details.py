name = input("Enter your Full Name : (FirstName-LastName):")
mobile = input("Enter your phone number:")
address = input("Ener your Address:")

print("----------------- User Enter Details ----------------")
print("Your entered values are")
print("User Full Name is:", name)
print("User Mobile no. is:", mobile)
print("User Address is:", address)
print("----------------- The End ----------------")

data = name.split("-")
# print("Splitted Data:", data)

if len(data) < 2:
    print("Invalid Name: Enter your Full Name in this format : (FirstName-LastName)")

if len(mobile) != 10:
    print("Invalid mobile number")
else:
    mobile = int(mobile)

if not address:
    print("Enter a valid Address") 
