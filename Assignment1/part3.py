def main():
    a = int(input("input a: "))
    b = int(input("input b: ")) 
    sum = 0
    for i in range(a,b + 1):
        if i %2 != 0:
            print (i)
            sum = sum + i
    print ("The sum of all number is:", sum)            
main()