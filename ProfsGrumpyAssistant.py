print("Welcome to the prof's office.")
print("I am his assistant.")
print("First you have to pass my quiz.")
print()

answer = input("In the game of chess, what color always moves first?\n")

if answer.lower() == "white":
    print("You got it correct! But that was only the warm-up...\n")
else:
    print("Wrong! Your chances of meeting the professor are slim now.")
    print()

word = input("Give me an 8-letter English word with at least 3 vowels.\n")

if len(word) == 8:
    print("Your word has 8 letters.")

    count_a = word.count('a')
    count_e = word.count('e')
    count_i = word.count('i')
    count_o = word.count('o')
    count_u = word.count('u')
    print()
    count_vowels = count_a + count_e + count_i + count_o + count_u
    print(count_a, count_e, count_i, count_o, count_u)
    print(count_vowels)

    if count_vowels>3:
        print("Oops...you gave me more than 3 vowels")
        print("You wasted my precious time! I only needed 3.")
    elif count_vowels<3:
        print("Oops...you gave me less than 3 vowels")
        print("You tried acting smart... I caught you.")
    else: 
        #Exactly 3 vowels
        print("What how... exactly 3 vowels")

