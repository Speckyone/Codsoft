import random
import string

def generate_password(length, include_special_chars=True):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    specials = string.punctuation if include_special_chars else ''

    all_chars = lower + upper + digits + specials

    if length < 1:
        raise ValueError("Password length must be at least 1.")

    password = ''.join(random.choice(all_chars) for _ in range(length))

    return password

def main():
    print("Password Generator")

    try:
        length = int(input("Enter the desired length of the password: "))
        include_special_chars = input("Include special characters? (yes/no): ").strip().lower() == 'yes'
    except ValueError:
        print("Invalid input. Please enter a numeric value for the length.")
        return

    if length < 1:
        print("Password length must be at least 1.")
        return

    password = generate_password(length, include_special_chars)
    print(f"\nGenerated Password: {password}")

if __name__ == "__main__":
    main()
