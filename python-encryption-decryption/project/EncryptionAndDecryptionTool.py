#Text Encryption and Decryption Tool

# 1-Caesar Cipher
def caesar_encrypt(text, shift):
    encryptedText = []
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            encryptedText.append(chr((ord(char) - base + shift) % 26 + base))
        else:
            encryptedText.append(char)
    return ''.join(encryptedText)

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)


# 2-Vigenère Cipher
def vigenere_encrypt(text, keyword):
    encryptedText = []
    keyword = keyword.lower()
    keyLength = len(keyword)
    keyIndex = 0

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shift = ord(keyword[keyIndex % keyLength]) - ord('a')
            encryptedText.append(chr((ord(char) - base + shift) % 26 + base))
            keyIndex += 1
        else:
            encryptedText.append(char)
    return ''.join(encryptedText)

def vigenere_decrypt(text, keyword):
    decryptedText = []
    keyword = keyword.lower()
    keyLength = len(keyword)
    keyIndex = 0

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shift = -(ord(keyword[keyIndex % keyLength]) - ord('a'))
            decryptedText.append(chr((ord(char) - base + shift) % 26 + base))
            keyIndex += 1
        else:
            decryptedText.append(char)
    return ''.join(decryptedText)

def menu():
    print("\n      Text Encryption and Decryption Tool      ")
    print("ec : Caesar Cipher Encryption")
    print("dc : Caesar Cipher Decryption")
    print("ev : Vigenère Cipher Encryption")
    print("dv : Vigenère Cipher Decryption")
    print("e  : Exit")
    return input("Choose an option (ec,dc,ev,dv,e) : ").strip()

def main():
    while True:
        choice = menu()
        if choice == "ec":
            text = input("Enter the text to encrypt: ").strip()
            shift = int(input("Enter the shift value for encrypt: ").strip())
            print("Encrypted Text:", caesar_encrypt(text, shift))
        elif choice == "dc":
            text = input("Enter the text to decrypt: ").strip()
            shift = int(input("Enter the shift value for decrypt: ").strip())
            print("Decrypted Text:", caesar_decrypt(text, shift))
        elif choice == "ev":
            text = input("Enter the text to encrypt: ").strip()
            keyword = input("Enter the keyword for encrypt: ").strip()
            print("Encrypted Text:", vigenere_encrypt(text, keyword))
        elif choice == "dv":
            text = input("Enter the text to decrypt: ").strip()
            keyword = input("Enter the keyword for decrypt: ").strip()
            print("Decrypted Text:", vigenere_decrypt(text, keyword))
        elif choice == "e":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()