def main():
    sum = 0
    for i in range (2,101):
        if i %2 == 0:
            print(i)
            sum+= i
    print ("Sum of all even number is:",sum)       
main()