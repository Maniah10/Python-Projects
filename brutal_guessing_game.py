import random
play = True
while play:
    number = random.randint(1,100)
    total_attemp = 3
    attempt = 0
    while True:
        while True:
            a = input("Enter your guess (1-100): ")
            try:
                a = int(a)
                break
            except ValueError:
                print("Enter  valid number!")
                continue


        if a == number:
            print(f"Congratulations!!! You guessed the right number in {attempt} attempts")
            break

        elif a > number:
            print("Too High")
            attempt += 1
            print(f"You have {total_attemp - attempt} attempts left!")
            
        elif a < number:
            print("Too low")
            attempt += 1
            print(f"You have {total_attemp - attempt} attempts left!")
            
        else:
            print("Invalid Error!")
            print(f"You have {total_attemp - attempt} attempts left!")
            
            
        if attempt >= total_attemp:
            print("Game over! You ran out of attempts!")
            print(f"The number was {number}!")  # reveling number
            break


    while True:
        b = input("Play again? (y/n): ").lower()
        if b == "y":
            break
        elif b == "n":
            play = False 
            break
            
        else:
            print("Enter y or n only!")
        


    

    
