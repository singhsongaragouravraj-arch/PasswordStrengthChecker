import string
import re
import random

def check_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"\d", password):
        score += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1

    if score <= 2:
        return "Weak"
    elif score == 3 or score == 4:
        return "Medium"
    else:
        return "Strong"

def generate_strong_password():
    all_chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choices(all_chars, k=12))

password = input("Enter password to check: ")
print("Strength:", check_strength(password))
print("Suggested strong password:")
