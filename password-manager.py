from cryptography.fernet import Fernet
print("Welcome to the game!! ")



'''def write_key():
     key = Fernet.generate_key()
     with open("key.key","wb") as key_file:
          key_file.write(key)'''

def load_key():
     file = open("key.key", "rb")
     key = file.read()
     file.close()
     return key


master_pwd = input("Enter your master password? ")
key = load_key() + master_pwd.encode()
fer = Fernet(key)


def add():
     name = input("Enter your name? ")
     pwd = input("Enter your password? ")

     with open("password.txt", "a") as f:
          f.write(name + "|" + fer.encrypt(pwd.encode()) + "\n")

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

     elif mode == "add":
          add()

     else:
        print("Enter valid option!!!")
        continue