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






    alice = {"firstName": "Alice",
        "lastName" : "Smith",
        "Major" : "Chemistry",
        "gpa" : 3.92,
        "courses" : ["CS 120", "CS124", "MATH 165"]
    }
    
    bob = {"firstName": "Bob",
        "lastName" : "Jones",
        "Major" : "Physics",
        "gpa" : 3.3,
        "courses" : ["CS222", "MATH 166"]
    }
    print(alice["courses"][2])
    for c in bob["courses"]:
        print(c)
    
main()