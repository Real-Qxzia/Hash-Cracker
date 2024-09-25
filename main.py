import hashlib

hash_type = input("Enter the type of hash to Crack (md5 or sha256): ").strip().lower()
hash_to_crack = input("Enter the Hash to Crack: ").strip()

if hash_type == "md5":
    with open('passwords.txt', 'r') as f:
        for line in f:
            password = line.strip()  # Strip whitespace/newline from the password
            encrypted_password = hashlib.md5(password.encode()).hexdigest()

            if hash_to_crack == encrypted_password:
                print(f"Successfully Cracked Password: {password}")
                break  # Exit loop if the password is cracked
        else:
            print("Hash Not Cracked")

elif hash_type == "sha256":
    with open('passwords.txt', 'r') as f:
        for line in f:
            password = line.strip()
            encrypted_password = hashlib.sha256(password.encode()).hexdigest()

            if hash_to_crack == encrypted_password:
                print(f"Successfully cracked password {password}")
                break
        else:
            print("Hash Not Cracked")
