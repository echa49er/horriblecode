import calculator

calculator = calculator.Calculator() #Creates calculator object

while True:
    selection = int(input("What would you like to do?\n 1. Addition\n 2. Subtraction\n 3. Multiplication\n 4. Division\n")) #Prints selection menu for user
    if selection == 1:
        calculator.addition() #Triggers addition function if user enters 1
    if selection == 2:
        calculator.subtraction() #Triggers subtraction function if user enters 2
    if selection == 3:
        calculator.multiplication() #Triggers multiplication function if user enters 1
    if selection == 4:
        calculator.division() #Triggers division function if user enters 1
    else:
        break #Any other number entered will end the program

