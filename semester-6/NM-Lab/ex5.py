def caesar_cipher(message, shift, mode='encrypt'):
    result = ""
    for char in message:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            shift_value = shift if mode == 'encrypt' else -shift
            result += chr((ord(char) - shift_base + shift_value) % 26 + shift_base)
        else:
            result += char
    return result

# Example usage
message = input("Enter the message: ")
shift = int(input("Enter the shift value: "))

# Encrypt the message
encrypted_message = caesar_cipher(message, shift, 'encrypt')
print(f"Encrypted message: {encrypted_message}")

# Decrypt the message
decrypted_message = caesar_cipher(encrypted_message, shift, 'decrypt')
print(f"Decrypted message: {decrypted_message}")
'''
Enter the message: hello world
Enter the shift value: 5
Encrypted message: mjqqt btwqi
Decrypted message: hello world


'''