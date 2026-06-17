def caesar_cipher(text, shift, mode):
    result = ""
    if mode == 'decrypt':
        shift = -shift
    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result

def main():
    print("=== Caesar Cipher Tool ===")
    while True:
        choice = input("\nDo you want to (e)ncrypt, (d)ecrypt, or (q)uit?: ").lower().strip()
        if choice == 'q':
            print("Exiting tool. Goodbye!")
            break
        if choice in ['e', 'd']:
            mode = 'encrypt' if choice == 'e' else 'decrypt'
            message = input("Enter your message: ")
            try:
                shift = int(input("Enter shift value (integer): "))
            except ValueError:
                print("Invalid shift value! Please enter a valid number.")
                continue
            output = caesar_cipher(message, shift, mode)
            print(f"\nResult ({mode}ed): {output}")
        else:
            print("Invalid option! Please choose e, d, or q.")

if __name__ == "__main__":
    main()