import random

name = input('What is your name: ')
print("Hello", name + '\n')

print("Choose difficulty(Easy or Hard): ")
diff = input()

if diff == "Easy":

    num1=int(input('Please tell me a number:\n'))
    num2=int(input('Please tell me another number:\n'))


    op = random.randint(0,2)
    if op == 0 :
        lhs = num1 + num2
        
    elif op == 1 :
        lhs = num1 - num2
    
    else:
        lhs = num1 * num2
    

    print("Can you tell me the missing operator? (+,-,*)")
    answer=input(str(num1) + '__' + str(num2) + ' = ' + str(lhs) + '\n') 

    if (answer== '+' and op==0) or (answer== '-' and op==1) or (answer== '*' and op==2):
        print("Good Job!")
    else:
        print("Better Luck Next Time!")

    num1=int(input('Please tell me a number:\n'))
    num2=int(input('Please tell me another number:\n'))


    op = random.randint(0,2)
    if op == 0 :
        lhs = num1 + num2
        
    elif op == 1 :
        lhs = num1 - num2
    
    else:
        lhs = num1 * num2
    

    print("Can you tell me the missing operator? (+,-,*)")
    answer=input(str(num1) + '__' + str(num2) + ' = ' + str(lhs) + '\n') 

    if (answer== '+' and op==0) or (answer== '-' and op==1) or (answer== '*' and op==2):
        print("Good Job!")
    else:
        print("Better Luck Next Time!")

elif diff == "Hard":

    n_numbers = 5
    list_numbers=[]
    list_ops=[]
    ops_str =[]
    for kk in range(n_numbers): 
        list_numbers.append(random.randint(1,100))

    for kk in range(n_numbers-1):
        list_ops.append(random.randint(0,1))
        # print(kk)

    # print(list_numbers)
    # print(list_ops)


    #Generate RHS

    rhs = list_numbers[0]
    for kk in range(len(list_ops)):
        if list_ops[kk] == 0:
            rhs = rhs + list_numbers[kk+1]
            ops_str.append("+")
        elif list_ops[kk] == 1:
            rhs = rhs - list_numbers[kk+1]
            ops_str.append("-")

    print()
    print("Can you tell the missing operators? (+ and -) ")

    qn = str(list_numbers[0])
    for i in range(n_numbers - 2):
        qn += str(list_numbers[i + 1])  + '__'

    qn += str(list_numbers[len(list_numbers) - 1]) + ' = ' + str(rhs) + '\n'
   

    answer = input(qn)
    answer_list = list(answer)
    # print(answer_list)



    #checking the answer

    for kk in range(n_numbers - 1):
        if answer_list[kk] == ops_str[kk]:
            if kk == n_numbers - 2:
                print("Good Job!")
        else:
            print("That's Incorrect")
            break
        
    n_numbers = 3
    list_numbers=[]
    list_ops=[]
    ops_str =[]
    for kk in range(n_numbers): 
        list_numbers.append(random.randint(1,30))

    for kk in range(n_numbers-1):
        list_ops.append(random.randint(0,1))
        # print(kk)

    # print(list_numbers)
    # print(list_ops)


    #Generate RHS

    rhs = list_numbers[0]
    for kk in range(len(list_ops)):
        if list_ops[kk] == 0:
            rhs = rhs + list_numbers[kk+1]
            ops_str.append("+")
        elif list_ops[kk] == 1:
            rhs = rhs - list_numbers[kk+1]
            ops_str.append("-")

    print()
    print("Can you tell the missing operators? (+ and -) ")

    qn= str(list_numbers[0]) + '__' + str(list_numbers[1]) + '__' + str(list_numbers[2]) + ' = ' + str(rhs) + '\n'

    answer = input(qn)
    answer_list = list(answer)
    # print(answer_list)


    #checking the answer

    for kk in range(n_numbers - 1):
        if answer_list[kk] == ops_str[kk]:
            if kk == n_numbers - 2:
                print("Good Job!")
        else:
            print("That's Incorrect")

            break


