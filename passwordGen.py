import random

def generate():
    characters = "0123456789abcdefghijklmnopqrstuvwxyz$@?()"
    length = 6
    password = ""

    for i in range(length):
        password += characters[random.randint(0, len(characters) - 1)]
    print("Your password is", password)

if __name__ == "__main__":
    generate()