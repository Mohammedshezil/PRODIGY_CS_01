import sys

# Sleek layout header 
def print_banner():
    print("-" * 60)
    print(" ██████╗ █████╗ ███████╗███████╗ █████╗ ██████╗      ██████╗██╗██████╗ ██╗  ██╗███████╗██████╗ ")
    print("██╔════╝██╔══██╗██╔════╝██╔════╝██╔══██╗██╔══██╗    ██╔════╝██║██╔══██╗██║  ██║██╔════╝██╔══██╗")
    print("██║     ███████║█████╗  ███████╗███████║██████╔╝    ██║     ██║██████╔╝███████║█████╗  ██████╔╝")
    print("██║     ██╔══██║██╔══╝  ╚════██║██╔══██║██╔══██╗    ██║     ██║██╔═══╝ ██╔══██║██╔══╝  ██╔══██╗")
    print("╚██████╗██║  ██║███████╗███████║██║  ██║██║  ██║    ╚██████╗██║██║     ██║  ██║███████╗██║  ██║")
    print(" ╚═════╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝     ╚═════╝╚═╝╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝")
    print("-" * 60)
    print("             PRODIGY INFOTECH CYBERSECURITY INTERNSHIP - TASK 01")
    print("-" * 60)

def caesar_cipher(text, shift, mode):
    result = ""
    # Adjust shift for decryption
    if mode == 'd':
        shift = -shift
        
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            # Handle alphabetical wrapping
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
    return result

def main():
    print_banner()
    while True:
        print("\n[1] Encrypt a Message")
        print("[2] Decrypt a Message")
        print("[3] Exit program")
        
        choice = input("\nSelect an option (1/2/3): ").strip()
        
        if choice == '1':
            message = input("\nEnter the secret message to encrypt: ")
            try:
                shift = int(input("Enter key shift value (integer): "))
                encrypted = caesar_cipher(message, shift, 'e')
                print(f"\n[+] Encrypted Result: {encrypted}")
            except ValueError:
                print("\n[-] Error: Shift value must be a valid number!")
                
        elif choice == '2':
            message = input("\nEnter the encrypted message to decrypt: ")
            try:
                shift = int(input("Enter matching shift value (integer): "))
                decrypted = caesar_cipher(message, shift, 'd')
                print(f"\n[+] Decrypted Result: {decrypted}")
            except ValueError:
                print("\n[-] Error: Shift value must be a valid number!")
                
        elif choice == '3':
            print("\nExiting. Stay secure!")
            sys.exit()
        else:
            print("\n[-] Invalid option! Please select 1, 2, or 3.")
            print("-" * 40)

if __name__ == "__main__":
    main()
