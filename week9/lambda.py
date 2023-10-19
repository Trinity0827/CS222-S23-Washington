#anaoymous function, no name, its a shorter function instead of doing def
add = lambda x,y: x + y
result = add(3,5)
print(result)

numbers = [1,2,3,4,5]
squareNumbers = list(map(lambda x: x**2, numbers))
print(squareNumbers)


fahTemp = [212,32,100]
celTemp = list(map(lambda f: (f-32)*5.0/9.0, fahTemp))
print(celTemp)


numbers = [3, 1, 5, 7, 8, 9]
sortedNumbers = sorted(numbers, reverse=True) #reverse counts it backwards
print(sortedNumbers)

midterm = {'Eve': 100, 'Alice': 98, 'Carol': 92,'Bob': 88,  'Dave': 70}
sortedScores = sorted(midterm.items(), key = lambda x  : x[1], reverse =True) #sorted by the value but it aorted by the key
print(sortedScores)                   #key is ther numbers   ----> numbers decreasing 


points = [(1,3,10),(2,1,20),(4,2,15)]
sortedPoints = sorted(points, key =lambda x : x[2])
print(sortedPoints)
