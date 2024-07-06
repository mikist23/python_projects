print("Welcome to the game!! ")
pwd = input("Enter your master password? ")


def add():
     pass

def view():
     pass

while True:
     mode = input("Do you want to view or add password (view,add) or q to quit").lower()

     if mode == "q":
          break
     
     if mode == "view":
          view()

     elif mode == add():
          add()

     else:
        print("Enter valid option!!!")
        continue