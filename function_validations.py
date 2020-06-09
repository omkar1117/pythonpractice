import sys


def is_filename_valid(output_file):
    x=False
    if output_file.endswith(".txt"):
        x=True
    return x
        
    # return True if output_file.endswith(".txt") else False


def render_input(val):
    d={}
    for row in val:
        x=input("Enter the :%s::"%row)
        d[row]=x
    return d


def name_validation(fn, ln):    
    return True if fn.strip() and ln.strip() else False


def writedata(data_file, op_filename):
    with open(op_filename, "w") as fp:
        
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


def handle():    
    if len(sys.argv) != 2:
        sys.exit()

    outputfile = sys.argv[1]
    
    if is_filename_valid(outputfile):
    
        data = render_input(
            ['fn', 'ln', 'email', 'phone', 'address',
             'loc', 'hobbies', 'sports']
            )
        if name_validation(data['fn'],data['ln']):
            writedata(data, outputfile)
        else:
            print("Name validation failed, First Name and Last Name are mandatory")
    else:
        print("Output File format is invalid , please enter a valid file format")
        

# handle()



        
