def main():
    try:
        studentList = open("students.txt", 'r') # reading is r
        students = studentList.readlines() # to read the file
        studentList.close()
        #print(students)
        for s in students:
            #print(s)
           parts = s.split() #spilt uses a space ot spilt up a string,| with commas use (' , ')
           #print(parts[0]) # first word in each line

           if parts[0] == "Smith": # print all names with the smith and info
               print(s)
    except FileNotFoundError:
        print("File not Found")
main()
