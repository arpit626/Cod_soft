import random
import string

def generate_password(length: int, complexity: int):
    # Define character sets based on complexity
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    punctuation = string.punctuation

    # Combine character sets based on complexity
    char_sets = [lowercase]
    if complexity >= 2:
        char_sets.append(uppercase)
    if complexity >= 3:
        char_sets.append(digits)
    if complexity >= 4:
        char_sets.append(punctuation)

    # Create a pool of characters
    all_chars = ''.join(char_sets)

    # Generate the password using random.choice
    password = ''.join(random.choice(all_chars) for _ in range(length))

    return password

def main():
    # User input for password length and complexity
    length = int(input("Enter the desired password length: "))
    complexity = int(input("Enter the complexity level (1-4, where 1 = lowercase, 2 = lowercase + uppercase, 3 = lowercase + uppercase + digits, 4 = all of the above): "))

    # Generate the password
    password = generate_password(length, complexity)

    # Display the password
    print(f"Generated password: {password}")

if __name__ == "__main__":
    main()
