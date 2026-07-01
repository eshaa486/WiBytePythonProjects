import random

print('Choose difficulty(Easy, Medium, or Hard): ')
diff = input()

if diff == "Easy":
    n = random.randint(1,50)
    print('I have picked a number between 1-50. Can you guess it?')

if diff == "Medium":
    n = random.randint(1,100)
    print('I have picked a number between 1-100. Can you guess it?')

if diff == "Hard":
    n = random.randint(1,250)
    print('I have picked a number between 1-250. Can you guess it?')


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


#Now user selects the number


print()
print()

print('Now your turn. You pick a number between 1-100')
print('Click ENTER when ready.')

input()
done = False
attempts = 0 
guess = random.randint(1,100)
guess_step = 10
prev_answer = ""

while not done:
    answer = input('Is it ' + str(guess) + '? (y = yes, l = less than that, g = greater than that)\n')
    attempts = attempts + 1

    print('attempts = ', attempts, 'prev_answer = ', prev_answer, 'answer = ', answer)

    if attempts > 1: 
        if prev_answer != answer:
            guess_step = guess_step - 1

    prev_answer = answer

    if answer == 'l':
        guess = guess - guess_step
        if guess < 1:
            guess = 1

    if answer == 'g':
        guess = guess + guess_step
        if guess > 100:
            guess = 100

    if answer == 'y':
        print('Yes, I got it correct!')
        print('I took ', attempts, 'attepts to guess this.')
        done = True


