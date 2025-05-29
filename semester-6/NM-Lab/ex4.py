import time

# Step 1: Define the secret key
secret_key = 123456

# Step 2: Define the OTP generator
def generate_otp():
    return str((int(time.time()) + secret_key) % 1000000).zfill(6)

# Step 3: Ask for password
password = input("Enter your password: ")

if password == "12345":
    otp = generate_otp()
    print(f"Your OTP is: {otp}")
    user_otp = input("Enter the OTP: ")
    
    if user_otp == otp:
        print("Authentication complete.")
    else:
        print("Invalid OTP.")
else:
    print("Incorrect password.")


'''
Enter your password: 12345
Your OTP is: 643284
Enter the OTP: 643284
Authentication complete.


'''