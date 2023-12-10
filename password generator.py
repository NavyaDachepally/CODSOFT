import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def password_generator():
    print("Password Generator")

    user_choice = input("Do you want to generate a random password (R) or input your own password (I)? ").upper()

    if user_choice == 'R':
        try:
            length = int(input("Enter the desired length of the password: "))
            if length > 0:
                password = generate_password(length)
                print("Generated Password:", password)
            else:
                print("Invalid length. Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    elif user_choice == 'I':
        user_password = input("Enter your own password: ")
        print("Your Password:", user_password)

    else:
        print("Invalid choice. Please enter 'R' for random password or 'I' for your own password.")

if __name__ == "__main__":
    password_generator()

