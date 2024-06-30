import random
import string

def generate_password(length):
    L = string.ascii_letters
    D = string.digits
    P = string.punctuation
    characters = L+D+P
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    print("Password Generator")
    try:
        print("Password length should be 8 Characters.")
        length = int(input("Enter the desired length of the password: "))
        if length <= 0:
            print("Please enter a positive integer for the length.")
            return
        if length>0 and length<8:
            print("Password length must be 8 or more than 8 Characters.")
            return
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        return
    
    password = generate_password(length)

    print("Generated Password:", password)

if __name__ == "__main__":
    main()
