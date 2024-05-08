from cryptography.fernet import Fernet
print("This is Vivek Singh Sisodiya Program")
def generate_key():
    key = Fernet.generate_key()
    return key

def encrypt(message,key):
    cipher_suite = Fernet(key)
    encrypted_message = cipher_suite.encrypt(message.encode())
    return encrypted_message

def decrypt(encrypted_message,key):
    cipher_suite = Fernet(key)
    decrypted_message = cipher_suite.decrypt(encrypted_message)
    return decrypted_message.decode()

# Generate a new encryption key
key = generate_key()

# Encrypt a message
message = "Why Hello Now"
encrypted_message = encrypt(message,key)
print("Encrypted message:", encrypted_message)

# Decrypt the message
decrypted_message = decrypt(encrypted_message,key)
print("Decrypted message:", decrypted_message)