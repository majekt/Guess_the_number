import time
import random

print('Hello!')
time.sleep(3)
print('I will generate the number between 1 and 100 and your task is to discover which number it is!')
time.sleep(3)
print('Ready? Okay, let\'s start!')
time.sleep(3)

number = random.randint(1, 100)
guess = int(input("Guess a number: "))

while guess != number:
    if guess < number:
        print("Too low!")
    else:
        print("Too high!")
    guess = int(input("Guess again: "))

print("Congratulations! You guessed the number.")