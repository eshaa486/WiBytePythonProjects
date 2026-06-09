import pyfiglet

print("Hello")
player = input('What is your name? ')
print("Hello", player)
print("We would like to quiz you")

print("A general knowledge quiz\n")
feeling = input('How are you feeling(G/B) ')
if(feeling == "G"):
    print("That's good\n")
elif(feeling == "B"):
    print("hope your feeling better\n")
else:
    print('Choose G or B')

 #Quiz Starting

 #Question 1
answer1 = input('What is the capital of France? (Rome or Paris)')
if(answer1 == "Paris"):
    result = pyfiglet.figlet_format("RIGHT",font = "letters")
    print(result)
else:
    result = pyfiglet.figlet_format("WRONG",font = "letters")
    print(result)

#Question 2

print('Next Question\n')

answer2 = input('Which planet is known as the Red Planet?(Mars or Jupiter) \n')
if(answer2 == "Mars"):
    result = pyfiglet.figlet_format("RIGHT",font = "letters")
    print(result)
else:
    result = pyfiglet.figlet_format("WRONG",font = "slant")
    print(result)

#Question 3

    print('Next Question\n')

    answer3 = input('What is the fastest land animal?(Cheetah or Lion) \n')
if(answer3 == "Cheetah"):
    result = pyfiglet.figlet_format("RIGHT",font = "letters")
    print(result)
else:
    result = pyfiglet.figlet_format("WRONG",font = "slant")
    print(result)


#Endgame
print('Good Job! You have finished the General Knowledge Quiz')

   
