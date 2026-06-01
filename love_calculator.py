import random
while True:
    a = input("Enter first name \n: ")
    if not a:
        print("You didn't enter anything")
        continue
    else:
        break
while True:  
    b = input("Enter second name \n: ")
    if not b:
        print("Again you didn't enter anything -_-")
        continue
    else:
        break
    
percentage = random.randint(1 , 100)
print("Love between",a,"and",b,"is", str(percentage) + "%")

