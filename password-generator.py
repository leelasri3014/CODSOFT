import secrets
import string

def generate_password(length):
    # Define the character sets for the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password using the specified length
    password = ''.join(secrets.choice(characters) for _ in range(length))

    return password

def main():
    print("Password Generator")
    
    try:
        # Get user input for the desired password length
        password_length = int(input("Enter the desired length of the password: "))
        
        # Check if the password length is valid
        if password_length <= 0:
            print("Invalid password length. Please enter a positive integer.")
            return

        # Generate and display the password
        generated_password = generate_password(password_length)
        print("\nGenerated Password:")
        print(generated_password)

    except ValueError:
        print("Invalid input. Please enter a valid integer for the password length.")

if __name__ == "__main__":
    main()
