
# [fn, ln, email, phone, address, loc, hobbies, sports]


def render_input(val):
    d={}
    for row in val:
        x=input("Enter the :%s::"%row)
        d[row]=x
    return d

data = render_input(
    ['fn', 'ln', 'email', 'phone', 'address', 'loc', 'hobbies', 'sports']
    )
print("Data Here is:",data)

def writedata(data_file):
    with open("output_data.txt", "w") as fp:
        
        y = 0        
        fn = data_file.pop("fn")
        ln = data_file.pop("ln")
        z = None
        fp.write("{}:  {}\n".format("Full Name".ljust(10), fn+" "+ln))
        for row, col in data_file.items():
            y+=1
            
            if y == 1:
                z = "{}:  {}\t".format(row.ljust(10),col.ljust(15))
                
            if y == 2:
                z += "{}:  {}\n".format(row.ljust(10),col)                
                fp.write(z)
                z=None
                y=0
                
        fp.close()

writedata(data)


        
