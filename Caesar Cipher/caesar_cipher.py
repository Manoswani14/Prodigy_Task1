def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    
    # Check mode and adjust shift for decryption
    if mode == 'decrypt':
        shift = -shift
    
    # Loop through each character in the text
    for char in text:
        if char.isalpha():
            # Shift character within the bounds of ASCII values for alphabets
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            # Non-alphabetic characters remain unchanged
            result += char
    
    return result

def main():
    print("Welcome to the Caesar Cipher Program!")
    mode = input("Do you want to (E)ncrypt or (D)ecrypt? ").strip().lower()
    
    if mode not in ['e', 'd']:
        print("Invalid choice! Please choose 'E' for encrypt or 'D' for decrypt.")
        return
    
    text = input("Enter your message: ").strip()
    shift = int(input("Enter the shift value: ").strip())
    
    if mode == 'e':
        encrypted_text = caesar_cipher(text, shift, mode='encrypt')
        print(f"Encrypted message: {encrypted_text}")
    else:
        decrypted_text = caesar_cipher(text, shift, mode='decrypt')
        print(f"Decrypted message: {decrypted_text}")

if __name__ == "__main__":
    main()
