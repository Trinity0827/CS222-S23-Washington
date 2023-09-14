def main():
    finalExamScores = {100, 82, 93, 81, 55, 72}
    print(finalExamScores[2:])  # ------>   83, 81, 55, 72, index 3,4,5, 6
    print(finalExamScores[:3])  # ------->  100, 82, 93 ,  index 0,1,2
    finalExamScores[3] = 10 #
    print(finalExamScores[1:4])  # --------> doesnt print index 1 or 4

    bsu = "Ball State University"
    bsu[2] = 'x'
    print (bsu[:12])  #----> stop at index 12
    print(bsu[-5]) # ----> start backwards  
    print(bsu[-5:-3]) # ----> start backwards rs
    for letter in bsu: # print out one at a time going down the line 
        print(letter)
    
main()