try:
    data = input("Enter the file name:")
    fp = open(data)
    fp.readline()
    
except IOError as err:
    print("OSError File not exists:: {0}, {1}, {2}, {3}".format(err,err,err,err))
