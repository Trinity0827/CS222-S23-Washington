def main():
    print("Lets find your BMI")
    height = int(input("Please enter your height (in)"))
    weight = int(input("Please enter your weight (lbs)"))
    x = (weight * 703)/(height)**2
    print(x)

    if x < 18.5:
        print("Underweight")
    if x > 25:
        return print("Overweight")
    if x >=18.5 and x<25:
        print("Optimal")   
main()