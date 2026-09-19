def calculator(operation,number1,number2):

    def addition():
        return f"Addition Result:{number1+number2}"

    def substraction():
        return f"Subtract Result:{number1-number2}"

    def division():
        return f"Division Result:{number1/number2}" if number2 !=0 else "Error: cannot divide by zero"

    def multiply():
        return f"Multiplication Result:{number1*number2}"

    if operation=="+":
        return addition()
    
    elif operation=="-":
        return substraction()

    elif operation=="/":
        return division()

    elif operation=="*":
        return multiply()
    else:
        return "Unknown Operation"


    