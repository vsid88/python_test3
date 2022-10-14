import random
number = random.randint(1, 10)

guesses = 0
while guesses < 5:
    guess = int(input("Enter a number:"))
    guesses += 1
    if guess < number:
        print('Guessed Number low')
    if guess > number:
        print('Guessed number high')
    if guess == number:
        break
if guess == number:
    print('You won ')
else:
    print('Please retry ' + str(number))