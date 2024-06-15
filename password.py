import random
import string

def generate_password(length):
    # Define character sets
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation
    
    # Combine all character sets
    all_characters = lower + upper + digits + special
    
    # Ensure at least one character from each set is included
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(special)
    ]
    
    # Fill the rest of the password length with random characters from the combined set
    password += random.choices(all_characters, k=length - 4)
    
    # Shuffle the list to ensure randomness
    random.shuffle(password)
    
    # Convert the list to a string
    return ''.join(password)

def main():
    print("Welcome to the Password Generator!")
    
    while True:
        try:
            length = int(input("Enter the desired length for the passwords (minimum 12 characters): "))
            if length < 12:
                print("Password length should be at least 12 characters. Please try again.")
                continue
            num_passwords = int(input("Enter the number of passwords you want to generate: "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    print("\nGenerated Passwords:")
    for _ in range(num_passwords):
        print(generate_password(length))

if __name__ == "__main__":
    main()