print("Welcome to the Game! ") 

import random

top_range = input("Type a number ? ")

if top_range.isdigit():
    top_range = int(top_range)

    if top_range <= 0 :
        print("Plesase type a number larger than zero next time")
        quit()

else:
    print("Plesase type a number next time")
    quit()
random_number = random.randint(0, top_range)

guesses = 0
while True:
    guesses +=1
    user_num = input("Make a guess ? ")
    if user_num.isdigit():
        user_num= int(user_num)
    else:
        print("Enter a number next time!!! ")
        continue  


    if user_num == random_number:
        print("You got it !!") 
        break
    else:
        print("Wrong!!!!")     

print("You got it after ", guesses, "guesses")