while True:  # infinite loop
    number = int(input("Enter a positive number: "))
    
    if number > 0:
        print("Good! You entered:", number)
        break  # exit the loop immediately
    
    print("Number is not positive. Try again ❌")
