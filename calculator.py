class Calculator:

    def __init__(self):
        pass

    def addition(self): #Calculates running total for user
        total = 0
        while True:
            value = input("Enter a number to add. When you're done, enter '0': ") #Promps user for numbers to add
            value_count = int(value)
            if value_count == 0: #If user enters a 0, break from the while loop
                break
            total += value_count #Else, keep adding user input into running total
        print("Your total sum is", total)
        return

    def subtraction(self): #Calculates running difference for user
        total = None
        while True:
            value = input("Enter a number to subtract. When you're done, enter '0': ") #Promps user for numbers to add
            value_count = int(value)
            if value_count == 0: #Breaks while loop if 0 is entered
                break
            if total is None:
                total = value_count #Sets first number in running difference to total
            else:
                total -= value_count #Keeps subtracting user input from total
        print("Your total difference is", total)
        return

    def multiplication(self): #Calculates total product
        total = 1  # Initialize total to 1 for multiplication
        while True:
            value = input("Enter a number to multiply. When you're done, please enter '-0': ") #Promps user for numbers to multiply
            value_count = int(value)
            if value_count == 0: #Breaks out of loop if user enters 0
                break
            total *= value_count  # Multiply the current total by the input value
        print("Your total product is", total)
        return

    def division(self):
        total = 1 # Initialize total to 1 for division
        while True:
            value = input("Enter a number to divide. When you're done, please enter '0': ") #Asks for user input for division (you get the gist)
            value_count = int(value)
            if value_count == 0: #Breaks out of loop if user enters 0
                break
            total /= value_count #Else, keep on with the running dividend
        print("Your total dividend is", round(total))
        return