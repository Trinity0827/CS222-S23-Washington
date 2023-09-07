def main():
    #finalExamScores = {100, 82, 93, 81, 55, 72} ----> List 
    finalExamScores = {
        "Alice" : 100,
        "Bob": 82, 
        "Carol": 93,
        "Dave": 81,
        "Eve": 55,
        "Frank": 72,
    }

    print("Gary" in finalExamScores.keys()) # give false
    print(finalExamScores.get('Carol')) # give the value
    print(finalExamScores.get('Harry'))


    

    #print(finalExamScores["Eve"])
    #finalExamScores["Eve"] = 57 #change the value 
    #print(finalExamScores["Eve"])

    #print all elment names in dic
    #for v in finalExamScores.values():
        #print(v)

    #print all keys in dic
    #for k in finalExamScores.keys():
        #print(k)

    #print both key and values
    #for key, value in finalExamScores.items():
       # print(value)

    students = [
        {
            "firstName": "Alice",
            "lastName" : "Smith",
            "Major" : "Chemistry",
            "gpa" : 3.92,
            "courses" : ["CS 120", "CS222", "MATH 165"]
        },
        {
        
            "firstName": "Bob",
            "lastName" : "Jones",
            "Major" : "Physics",
            "gpa" : 3.3,
            "courses" : ["CS222", "MATH 166"]
        }
    ]

    print(len(students)) 
    for s in students:
        #if s["Major"] == "Physics" : # each item in the list
         #   print(s["lastName"]+ " , " + s ["firstName"])
       # if (s["gpa"]) > 3.5:
         #  print(s)
        if "CS 222" in s["courses"]: # anything with CS in that major 
            print(s["lastName"] + " , " + s ["firstName"])


    #print(alice["courses"][2])
    #for c in bob["courses"]:
      #  print(c)
    
main()