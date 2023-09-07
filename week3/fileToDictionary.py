def main():
    students = {}
    fileHandle = open("students.txt", "r")
    fileData = fileHandle.readLines()


    for lines in fileData:
        parts = lines.spilt(' , ')
        print(parts)
        students[parts[0]] = parts[1], parts[2], parts[3], parts[4]
        
    fileHandle.close()
    print(students)
main()