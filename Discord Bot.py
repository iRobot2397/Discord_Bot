def calculator():

    operation = input("Which operation would you like to do(+, -, *, /): ")
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))
    whole = input("Would you like to round to a whole number(y/n): ")
    #addition
    if operation == "+":
        number3 = number1 + number2
        if whole == "y":
          number3 = int(number3)
          print("The answer is {}".format(number3))
        else:
          print("The answer is {}".format(number3))
    #subtraction
    elif operation == "-":
        number3 = number1 - number2
        if whole == "y":
          number3 = int(number3)
          print("The answer is {}".format(number3))
        else:
          print("Your answer is {}".format(number3))
    #multiplaction
    elif operation == "*":
        number3 = number1 * number2
        if whole == "y":
          number3 = int(number3)
          print("The answer is {}".format(number3))
        else:
          print("Your answer is {}".format(number3))
    #division
    elif operation == "/":
        number3 = number1 / number2
        if whole == "y":
          number3 = int(number3)
          print("The answer is {}".format(number3))
        else:
          print("Your answer is {}".format(number3))

    else:
        print("Your operation is invalid, please try again.")
        calculator()


calculator()

again = input("Would you like to use the calculator again?(y/n): ").lower()
again = again.lower()

if again == "y":
    print("Okay")
    calculator()
    again = input("Would you like to use the calculator again?(y/n): ").lower()
    again = again.lower()
    
    if again == "y":
      print("Okay")
      calculator()
      again = input("Would you like to use the calculator again?(y/n): ").lower()
      again = again.lower()


    elif again == "n":
      print("Thank you for using the calculator, I hope you come back!")

    else:
      print("Invalid input please try again.")
      again = input("Would you like to use the calculator again?(y/n): ")


elif again == "n":
    print("Thank you for using the calculator, I hope you come back!")

else:
    print("Invalid input please try again.")
    again = input("Would you like to use the calculator again?(y/n): ")