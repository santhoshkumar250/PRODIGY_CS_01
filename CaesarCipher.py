def caesar_cipher(text, shift, mode='encrypt'):
    """
    Encrypts or decrypts a given text using the Caesar Cipher algorithm.

    :param text: The input text to encrypt or decrypt.
    :param shift: The shift value for the cipher.
    :param mode: 'encrypt' to encrypt or 'decrypt' to decrypt.
    :return: The encrypted or decrypted text.
    """
    if mode == 'decrypt':
        shift = -shift

    result = ''
    for char in text:
        if char.isalpha():
            # Determine if the character is uppercase or lowercase
            base = ord('A') if char.isupper() else ord('a')
            # Shift the character and wrap around the alphabet
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            # Non-alphabetic characters remain unchanged
            result += char
          
    return result

# Main program
if __name__ == "__main__":
    print("Welcome to the Caesar Cipher program!")
    while True:
        print("\nChoose an option:")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ").strip()

        if choice == '1':
            text = input("Enter the message to encrypt: ")
            shift = int(input("Enter the shift value: "))
            encrypted_text = caesar_cipher(text, shift, mode='encrypt')
            print(f"Encrypted message: {encrypted_text}")
        elif choice == '2':
            text = input("Enter the message to decrypt: ")
            shift = int(input("Enter the shift value: "))
            decrypted_text = caesar_cipher(text, shift, mode='decrypt')
            print(f"Decrypted message: {decrypted_text}")
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
