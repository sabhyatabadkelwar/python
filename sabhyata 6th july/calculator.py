print(" This is my simple calculator ")
while True:
    print(" press 1 for addition ")
    print(" press 2 for subtraction ")
    print(" press 3 for multiplication ")
    print(" press 4 for division ")
    print(" press 5 for modulus ")
    print(" press 6 for exponent multiplication ")
    print(" press 7 for exponent division ")
    print(" press 8 for exit ")
    choice = input()
    if choice =='1':
        number1 = int(input(" please enter the number1: "))
        number2 = int(input(" please enter the number2: "))
        print(f" the sum of {number1} and {number2} is ", number1+number2)
    elif choice =='2':
        number1 = int(input(" please enter the number1: "))
        number2 = int(input(" please enter the number2: "))
        print(f" the subtraction of {number1} and {number2} is ", number1-number2)
    elif choice =='3':
        number1 = int(input(" please enter the number1: "))
        number2 = int(input(" please enter the number2: "))
        print(f" the multiplication of {number1} and {number2} is ", number1 * number2)
    elif choice =='4':
        number1 = int(input(" please enter the number1: "))
        number2 = int(input(" please enter the number2: "))
        print(f" the division of {number1} and {number2} is ", number1/number2)
    elif choice =='5':
        number1 = int(input(" please enter the number1: "))
        number2 = int(input(" please enter the number2: "))
        print(f" the modulus of {number1} and {number2} is ", number1%number2)
    elif choice =='6':
        pass
    elif choice =='7':
        number1 = int(input(" please enter the number1: "))
        number2 = int(input(" please enter the number2: "))
        print(f" the exponent division of {number1} and {number2} is ", number1//number2)
    elif choice=='8':
        break
    else:
        print(" please enter a valid choice")
