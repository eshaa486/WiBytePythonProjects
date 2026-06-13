name = input('What is your name: ')
print("Hello", name)



import random


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

# num1=int(input('Please tell me a number:\n'))
# num2=int(input('Please tell me another number:\n'))


# op = random.randint(0,2)
# if op == 0 :
#     lhs = num1 + num2
    
# elif op == 1 :
#     lhs = num1 - num2
  
# else:
#     lhs = num1 * num2
   

# print("Can you tell me the missing operator? (+,-,*)")
# answer=input(str(num1) + '__' + str(num2) + ' = ' + str(lhs) + '\n') 

# if (answer== '+' and op==0) or (answer== '-' and op==1) or (answer== '*' and op==2):
#     print("Good Job!")
# else:
#     print("Better Luck Next Time!")


n_numbers = 3
list_numbers=[]
list_ops=[]
for kk in range(n_numbers): 
    list_numbers.append(random.randint(1,30))

for kk in range(n_numbers-1):
    list_ops.append(random.randint(0,1))


#Generate RHS

rhs = list_numbers[0]
for kk in range(len(list_ops)):
    if list_ops[kk] == '+':
        rhs = rhs + list_numbers[kk+1]


print()
print("Can you tell the missing operators? (+ and -)")

qn=''

for kk in range(n_numbers): 
    if kk<= n_numbers - 2:
        qn = qn + str(list_numbers[kk]) + ' = ' + str(rhs) + '\n'

answer = input(qn)


#checking the answer

for kk in range(n_numbers - 1):
    if answer[kk] == list_ops[kk]:
        if kk == n_numbers - 2:
            print("Good Job!")
    else:
        print("That's Incorrect")