def main():
    #for x in range(3): #runs outisde loop 3 times  
       # for y in range(2): #run inside loop 2 times 
           # print ("BSU") # = 6


    #for x in range(3): #runs outisde loop 3 times  
       # for y in range(2): #once it hits 1 it not runnig tthe inside loop 
           # if y ==1:
                #break 
    
            #print ("BSU") # = 3

    for counter in range(5):  
        if counter == 2 or counter == 3: 
            continue # it skips 2 and 3, 5-2 = 3
            print ("BSU") # = 3

main()