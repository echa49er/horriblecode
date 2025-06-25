class Calculator:

    def __init__(self):
        pass

    def addition(self):
        total = 0
        while True:
            value = input("Enter a number to add. When you're done, enter '0': ")
            value_count = int(value)
            if value_count == 0:
                break
            total += value_count
        print("Your total sum is", total)
        return

    def subtraction(self):
        total = None
        while True:
            value = input("Enter a number to subtract. When you're done, enter '0': ")
            value_count = int(value)
            if value_count == 0:
                break
            if total is None:
                total = value_count
            else:
                total -= value_count
        print("Your total difference is", total)
        return

    def multiplication(self):
        total = 1  # Initialize total to 1 for multiplication
        while True:
            value = input("Enter a number to multiply. When you're done, please enter '-0': ")
            value_count = int(value)
            if value_count == 0:
                break
            total *= value_count  # Multiply the current total by the input value
        print("Your total product is", total)
        return

    def division(self):
        total = 1
        while True:
            value = input("Enter a number to divide. When you're done, please enter '0': ")
            value_count = int(value)
            if value_count == 0:
                break
            total /= value_count
        print("Your total dividend is", round(total))