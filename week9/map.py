def square(x):
    return x**2  #muliply the nubers by itself
numbers = [1,2,3,4,5]
squares = map(square, numbers)
squaresList = list(squares)
print(squaresList)


fruits = ["apple", "banana", "cherry"]
wordLengths = list(map(len, fruits)) #matching each fruit to the length --> apple=5,banana=6,cherry=6
print(wordLengths)

def ConvertToUpper(str):
    return str.upper()

names = ["alice", "bob", "carol", "dave", "eve"]
uppercaseNames = list(map(ConvertToUpper ,names))
print(uppercaseNames)

def FahToCel(fah):
    return (fah - 32) * 5.0/9.0

FahTemperature = [212,32,100]
CelTemperature = list(map(FahToCel, FahTemperature))
print(CelTemperature)