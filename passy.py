import random

user_info = ['Ashutosh', 'RAHUL', 'Omkar', '@!$', '#%&', '*#@!', 'ABHISHEK', 'Mohit', 'HARSHIT']
from_input = []                             #Created a list to add input from user
temp = ''

placeName = input("For which place you are creating Password: ")
if placeName == "Gmail":
    emailId = input("Please enter your email id: ")
    from_input.extend([placeName, emailId])
    
else:
    from_input.extend([placeName])
    

list3 = list(user_info + from_input)


for i in list3:
    temp = temp + random.choice(i)

f = open('Password.txt', 'a')
f.write('\n')
f.write(f'For: {placeName} and Password is: {temp}')
f.close()
print(f'Password created successfully: {temp}')