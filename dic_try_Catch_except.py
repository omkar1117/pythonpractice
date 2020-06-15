def divide(x,y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("Can't divide with zero")

    except Exception as e:
        print("Exception Here:", e)
        
    else:
        print("Div result here::", result)
    finally:
        print("End of finally block")

    
divide("2", "1")
