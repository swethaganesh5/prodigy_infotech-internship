def caesar_cipher_encrypt(message, shift):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            shift_amount = shift % 26
            new_char = ord(char) + shift_amount
            if char.islower():
                if new_char > ord('z'):
                    new_char -= 26
                encrypted_message += chr(new_char)
            elif char.isupper():
                if new_char > ord('Z'):
                    new_char -= 26
                encrypted_message += chr(new_char)
        else:
            encrypted_message += char
    return encrypted_message

def caesar_cipher_decrypt(message, shift):
    return caesar_cipher_encrypt(message, -shift)

def main():
    while True:
        choice = input("Do you want to (e)ncrypt or (d)ecrypt a message? (e/d): ").lower()
        if choice in ['e', 'd']:
            message = input("Enter the message: ")
            shift = int(input("Enter the shift value: "))
            if choice == 'e':
                result = caesar_cipher_encrypt(message, shift)
                print("Encrypted message:", result)
            else:
                result = caesar_cipher_decrypt(message, shift)
                print("Decrypted message:", result)
        else:
            print("Invalid choice. Please enter 'e' to encrypt or 'd' to decrypt.")

        another = input("Do you want to process another message? (yes/no): ").lower()
        if another != 'yes':
            break

if __name__ == "__main__":
    main()
