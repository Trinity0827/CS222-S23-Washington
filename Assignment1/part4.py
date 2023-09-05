def main():
  
  target = float(input("Enter target price: "))
  while True:
    currentPrice = float(input("Enter the current stock price: "))

    if(target <= currentPrice):
       print('Shares can be sold now')
       break
    else: 
      print("Try again")
main()