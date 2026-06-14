import random
number = random.randint(1, 10)
while True:
    while True:
        guess = input("Guess the number \n:")
        try:
            guess = int(guess)
            break
        except:
            print("Enter number only!")
            continue

    if guess == number:
        print("Congratulations! , You guessed the right number")
        break
    elif guess > number:
        print("📈 Too high! Go lower!")
    elif guess < number:
        print("📉 Too low! Go higher!")
