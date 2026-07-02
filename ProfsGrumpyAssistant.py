import datetime as dt

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
    # print(count_a, count_e, count_i, count_o, count_u)
    # print(count_vowels)

    if count_vowels>3:
        print("Oops...you gave me more than 3 vowels")
        print("You wasted my precious time! I only needed 3.")
    elif count_vowels<3:
        print("Oops...you gave me less than 3 vowels")
        print("You tried acting smart... I caught you.")
    else: 
        #Exactly 3 vowels
        print("What how... exactly 3 vowels")
else:
    print("You seem to be a disaster...")
    print("Your word does not even have 8 letters.")

print()

sentence= input("ok, tell me a sentence ending in wise assistant (no questions please)\n")

if sentence.endswith("wise assistant"):
    print("Have you not learnt about punctuations?")
elif sentence.endswith("wise assistant."):
    print("That sentence looks ok... but... wait...")
    len_first = sentence.find('')
    if len_first < 7:
        print("The first word in your sentence was too short.")
else:
    print("You will really make the prof furious")

ct1 = dt.datetime.now()
sentence= input("ok, tell me a sentence ending in at the end of the day (no questions please)\n")
ct2 = dt.datetime.now()

diff = ct2 - ct1
if diff.seconds < 10:
    print("What..",diff.seconds, " seconds, that was too fast\n")
elif diff.seconds > 10:
    print("What..",diff.seconds, " seconds to answer that ... very bad\n")
elif diff.seconds == 10:
    print("What...",diff.seconds, " seconds to answer that ... very bad\n")



#Appointment
print("Ok... I admit defeat, pick a time next monday to meet the professor.")
print("A. 8 mins past midnight", "B. 16 mins before sunrise", sep='\t\t')
print("C. 24 mins before noon", "D. 48 mins after sunset", sep='\t\t')


print()

appointment = input("Please select your slot (A/B/C/D)\n")

if appointment == "A":
    print("Careful, Professor may be asleep")
elif appointment == "B":
    print("Warning, Professor may be jogging")
elif appointment == "C":
    print("Beware, Professor may be hungry")
else:
    print("Caution, Professor may be tired")


print()

print("Good luck for your appointment! Bye for now.")






        


