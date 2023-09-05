def main():
    fileData = open("student.txt", "r") # ---> read
    students = fileData.readlines()
    fileOutput = open("out.put.txt", "w") # ---> write
    for s in students:
        parts = s.spilt (' , ')
        # print(parts)
        gpa = float(parts[3]) # only print the 3 elment --> the numbers
        fileOutput.write(parts[1] + " ' s GPA is " + str(gpa) + " \n")
        print(gpa)
        
        fileData.close()
        fileOutput.close()
main()