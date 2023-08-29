def main():
    for counter in range(10):
        print("BSU")
        if counter == 5: #stops when the loop hits 5 -> 0,1,2,3,4,5 = 6
            break #Stops 

    for counter in range(10):
        if counter == 5: #print 5 only
            break 
        print("BSU")


main()