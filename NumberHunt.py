import random
n = random.randint(1,100)

print('I have picked a number between 1-100. Can you guess it?')


attempts = 0
done = False
while not done:
    guess = int(input('Guess the number?\n'))
    attempts = attempts + 1

    if guess > n:
        print('My number is less than that.\n')

    if guess < n:
        print('My number is greater than that.\n')

    if guess == n:
        print('You have guessed the number correctly!')
        print('You took', attempts, 'attempts to guess this.\n')
        done = True
