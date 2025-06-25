import random
import string

def generate_password(length=12):
    if length < 4:
        raise ValueError("Password length should be at least 4 characters.")

    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Combine all characters
    all_chars = lowercase + uppercase + digits + symbols

    # Ensure at least one character from each type
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(symbols)
    ]

    # Fill the remaining characters randomly
    password += random.choices(all_chars, k=length - 4)

    # Shuffle to make it unpredictable
    random.shuffle(password)

    return ''.join(password)

# Auto-generate password
auto_password = generate_password(12)  # You can change length here
print("Generated Password:", auto_password)
