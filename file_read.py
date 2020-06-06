fname = input("Enter the filename to read:")
fr = open(fname)
data = fr.readlines()
fr.close()

l=[]
for row in data:
    if not '----' in row:
        details={}        
        if 'First Name' in row:
            details['first_name']= row.split("::")[1].rstrip().lstrip()
        if 'Last Name' in row:
            details['last_name'] = row.split("::")[1].rstrip().lstrip()
        if 'Email' in row:
            details['email'] = row.split("::")[1].rstrip().lstrip()
        l.append(details)
        
        #print("Details::", details)
print("List Here", l)

