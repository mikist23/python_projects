print("Welcome to the game!! ")
master_pwd = input("Enter your master password? ")


def add():
     name = input("Enter your name? ")
     pwd = input("Enter your password? ")

     with open("password.txt", "a") as f:
          f.write(name + "|" + pwd + "\n")

def view():
     with open("password.txt", "r") as f:
          for line in f.readlines():
               data = line.rstrip()
               if "|" in data:
                        try:
                          user, passw = data.split("|")
                          print("User: ", user, "Password: ", passw)
                        except ValueError:
                         print(f"Skipping malformed line: {data}")
                
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