import random

print("This is Mohd Afzal Program")
def generate_otp():
    otp = random.randint(1000, 9999)
    return otp

def send_otp(otp):
    # Code to send the OTP to the user (e.g., via email, SMS, etc.)
    print(f"OTP sent: {otp}")

def verify_otp(otp, user_input):
    if otp == int(user_input):
        print("OTP verification successful!")
    else:
        print("OTP verification failed!")

# Generate and send OTP
otp = generate_otp()
send_otp(otp)

# Prompt user to enter OTP
user_input = input("Enter the OTP: ")

# Verify OTP
verify_otp(otp, user_input)