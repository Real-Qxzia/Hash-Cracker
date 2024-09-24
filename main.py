import hashlib

hash_to_crack = input("Enter the Hash to Crack: ").strip()
with open('passwords.txt', 'r') as f:
    for line in f:
        password = line.strip()  # Strip whitespace/newline from the password
        encrypted_password = hashlib.md5(password.encode()).hexdigest()
        
        if hash_to_crack == encrypted_password:
            print(f"Successfully Cracked Password: {password}")
            break  # Exit loop if the password is cracked
    else:
        # This else block executes if the loop completes without break
        print("Hash Not Cracked")
