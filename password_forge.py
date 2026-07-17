import secrets
import string

def generate_password(length=12, use_upper=True, use_digits=True, use_symbols=True):
    # Base character set
    chars = string.ascii_lowercase
    
    if use_upper:
        chars += string.ascii_uppercase
    if use_digits:
        chars += string.digits
    if use_symbols:
        chars += string.punctuation
    
    if not chars:
        raise ValueError("No character sets selected for password generation.")
    
    # Secure random choice
    password = ''.join(secrets.choice(chars) for _ in range(length))
    return password

if __name__ == "__main__":
    # Example usage
    print("🔑 Strong password:", generate_password(length=16))
    print("🔑 Digits only:", generate_password(length=10, use_upper=False, use_symbols=False))
    print("🔑 Minimal symbols:", generate_password(length=20, use_symbols=False))
