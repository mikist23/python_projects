print("Welcome to the game!! ")
master_pwd = input("Enter your master password? ")


def add():
     name = input("Enter your name? ")
     pwd = input("Enter your password? ")

     with open("password.txt", "a") as f:
          f.write(name + "|" + pwd)

def view():
     pass

while True:
     mode = input("Do you want to view or add password (view,add) or q to quit? ").lower()

     if mode == "q":
          break
     
     if mode == "view":
          view()

     elif mode == add():
          add()

     else:
        print("Enter valid option!!!")
        continue