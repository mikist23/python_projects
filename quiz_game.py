print("Welcome to the Game! ") 

playing = input("Do you want to play the game! ")

if playing.lower() != "yes":
    quit()

print("Let's play the Game! ")
score  =0


answer = input("What does CPU mean in computig ? ") 
if answer.lower() == "central processing unit":
    print("Correct! ")
    score  += 1
else:
    print("Incorrect! ")  

answer = input("What does GPU stand for ? ") 
if answer.lower() == "graphics processing unit":
    print("Correct! ")
    score  += 1
else:
    print("Incorrect! ")          


answer = input("What does PSU stand for ?") 
if answer.lower() == "power supply unit":
    print("Correct! ")
    score  += 1
else:
    print("Incorrect! ")  

answer = input("What is Python in computing ? ") 
if answer.lower() == "programming language":
    print("Correct! ")
    score  += 1
else:
    print("Incorrect! ")  


print("You Got " + str(score) + "Correct")
print("Your score is " + str((score/4) *100) + "%")    


