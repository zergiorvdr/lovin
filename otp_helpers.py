import random
import string

def generate_otp():
    otp = ''.join(random.choices(string.digits, k=6))
    return otp

def validate_otp_format(otp):
    return otp.isdigit() and len(otp) == 6

def validate_otp(stored_otp, user_input):
    return stored_otp == user_input
