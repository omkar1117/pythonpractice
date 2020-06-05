import sys

name = input("Enter your First Name:")
lname = input("Enter your Last Name:")
email = input("Enter a valid Email:")
mobile = input("Enter a Valid No:")

if not name or not lname or not email or not mobile:
    print("You need to enter all values")
    sys.exit(0)

l=[name, lname, email, mobile]
print("Your values have been registered")
print("Values Here:", l)

gender = input("Enter Your Gender in the Values of M/F ::")
l.append(gender)

print("Values Updated Here", l)

# First - Last (0 - 9) List with 10 elements.
# Last - First (-10 -  -1) If we have a list with 10 elements.

x = l[-1]
print("Element as Last index of List:", x)

# pop element from Last index of List
l.pop()

print("Data after removing last element in List:", l)

#Inserting element Gender at Starting Point of List
l.insert(0, x)

print("After entering data to List:", l)
