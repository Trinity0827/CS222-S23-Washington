def main():
    midterm = [70, 92, 100]
    try:
        print (midterm [2])
    except:
        print("Something went wrong")
    x = 0
    try: # if its not diving by zero it priniting "you are..."" else wise "CS 222"
        z = 10 / x
    except ZeroDivisionError:
        print("You are dividing by zero")
    except NameError:
        print("Name error")
    else:
        print("CS 222")
    finally: #run no matter what
        print("BSU")
main()