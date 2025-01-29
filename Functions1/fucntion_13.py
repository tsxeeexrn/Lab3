import random
n = random.randint(1, 20)
print("Hello! What is your name? ")
name = input()
print("Well, KBTU, I am thinking of a number between 1 and 20. ")
print("Take a guess. ")
while True:
    number = input("Your number: ")
    if number == 'q':
        print("Exit")
        break
    number = int(number)
    if number > n:
        print("Too high")
    elif number < n:
        print("Too low")
    else:
        print("Good job, KBTU! You guessed my number!")
        break