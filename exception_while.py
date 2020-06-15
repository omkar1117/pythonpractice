while True:
    try:
        x = int(input("Enter a number:"))
        break
    except ValueError:
        print("We're expecting a Valid integer....")
