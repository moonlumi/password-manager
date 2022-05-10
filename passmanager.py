
#importing module to encrypt passwords
from cryptography.fernet import Fernet

# generating the key
"""def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)"""


def load_key():
    key = open("key.key", "rb").read()
    return key


master_pass = input("Enter master password :")
key=load_key()+master_pass.encode()
fer=Fernet(key)

def add():
    name = input("Enter Platform: ")
    password = input("Enter password: ")

    with open("pass_manager.txt", "a") as f:

        f.write(name + "|" + fer.encrypt(password.encode()).decode() + "\n")


def view():
    with open("pass_manager.txt", "r") as f:
        for i in f.readlines():
            info = i.rstrip()
            user, passw = info.split("|")
            print("Username: ", user, "| Password: ",fer.decrypt(passw.encode()).decode())


# taking master password as input
while True:
    mode = input(
        "Do you want to add new password or view existing ones(add/view). Press q to quit :"
    )
    if mode == "q":
        break

    elif mode == "add":
        add()
    elif mode == "view":
        view()
    else:
        print("Invalid response")
