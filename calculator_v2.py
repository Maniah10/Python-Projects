
# Successfully created def function to use code repetedly
def calculate (first_number , sign , second_number):
    try:
        a = float(first_number)
        b = float(second_number)
    except ValueError:
        pass
    if sign == "+":
        result = a  + b 
    elif sign == "-":
        result = a  - b 
    elif sign == "*":
        result = a  * b 
    elif sign == "/":
        result = a  / b 
    elif sign == "//":
        result = a  // b 
    elif sign == "**":
        result = a  ** b 
    return result


# Looping in to contine the process
while True:
    first  = input("First number:  ")
    sign = input("Sign:  ")
    second = input("Second number:  ")


    # Calculation Command
    result = calculate(first , sign , second)


    # Adjusting the type of result
    if result == int(result):
        print(int(result))
    else:
        print(result)
    

    # Asking for continue
    again = input("Continue? (y/n): ").lower()
    if again == "n":
        break







        