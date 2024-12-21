import random
import string


print("Developer: Warda Mehboob")
print("Registration Number: F2021065208")  

def generate_password(length=12):
    if length < 12:
        raise ValueError("Password length must be at least 12 characters for security.")
    
   
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = "!@#$%^&*()-_=+"

   
    all_chars = random.choice(lower) + random.choice(upper) + random.choice(digits) + random.choice(special)

    remaining_length = length - len(all_chars)
    all_chars += ''.join(random.choices(lower + upper + digits + special, k=remaining_length))

   
    password = ''.join(random.sample(all_chars, len(all_chars)))

    return password


try:
    password = generate_password(16)  
    print(f"Generated Password: {password}")
except Exception as e:
    print(f"Error: {e}")

print("Developer: Warda Mehboob")
print("Registration Number: F2021065208") 