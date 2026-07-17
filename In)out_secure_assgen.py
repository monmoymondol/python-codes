import secrets
import string

def generate_password(length=12, use_upper=True, use_digits=True, use_symbols=True):
    chars = string.ascii_lowercase
    
    if use_upper:
        chars += string.ascii_uppercase
    if use_digits:
        chars += string.digits
    if use_symbols:
        chars += string.punctuation
    
    if not chars:
        raise ValueError("No character sets selected for password generation.")
    
    password = ''.join(secrets.choice(chars) for _ in range(length))
    return password

if __name__ == "__main__":
    print("🔑 Password Generator")
    length = int(input("Enter password length: "))
    
    use_upper = input("Include uppercase letters? (y/n): ").lower() == "y"
    use_digits = input("Include digits? (y/n): ").lower() == "y"
    use_symbols = input("Include symbols? (y/n): ").lower() == "y"
    
    password = generate_password(length, use_upper, use_digits, use_symbols)
    print("\n✅ Your generated password:")
    print(password)
