# Created veriable to store history of calculaation 
history = []

# Creating def function 
def calculate(first_number , sign , second_number):
    try:
        a = float(first_number)             #}First number
        b = float(second_number)            #}Second number
    except ValueError:
        return "Error: Invalid number!"

    # Sign and calculaton logic
    if sign == "+":
        return a + b 
    elif sign == "-":
        return  a - b
    elif sign == "*":
        return a * b
    elif sign == "/":
        if b == 0:
            return "Error: Cannot divide by zero!"
        return  a / b
    elif sign == "//":
        if b == 0:
            return "Error: Cannot divide by zero!"
        return  a // b
    elif sign == "**":
        return  a ** b
    else:
        return "Error: Invalid sign!"


# looping the input function.
while True:   
    # Asking for input 
    first = input("First Number :  ")
    sign = input("Sign :  ")
    second = input("Second Number :  ")

    # Acctual calculation, callind def function here
    result = calculate(first , sign , second)


    #storing elemnt in veriable name history as a list 
    history.append([first, sign, second, result])


    # Convert the answer into int otherwisw print as it is
    try:
        if result == int(result):
            print(int(result))
    except:
        print(result)
            
    
    # Question Block
    question = input("Do you want to continue y/n:  \npress h to check history:  ").lower()
    
    # To check history
    if question == "h":
        print("----Histry----")
        for item in history:
            print(item[0],item[1],item[2],'=',item[3])

    # continue or stop?
    if question == 'n':
        break





        

        

