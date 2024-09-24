# 📜 MD5 Hash Cracker 🔒

## Table of Contents
1. [Overview](#overview)
2. [Prerequisites](#prerequisites)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Code Explanation](#code-explanation)
6. [Detailed Breakdown](#detailed-breakdown)
7. [Contributing](#contributing)
8. [License](#license)

---

## Overview
The **MD5 Hash Cracker** is a Python script designed to reverse-engineer MD5 hashes by comparing them against a list of potential plaintext passwords sourced from a local file. This utility serves as a demonstration of hash cracking techniques, showcasing the vulnerabilities associated with MD5 hashing when used for password storage.

---

## Prerequisites
Before utilizing this script, ensure that the following prerequisites are met:

- **Python 3.x**: The script is compatible with Python 3 and should be executed in an environment where Python is installed.
- **passwords.txt**: A text file containing potential passwords, one per line.

---

## Installation
To install the necessary components for running this script, execute the following commands in your terminal:

```bash
# Clone the repository
git clone https://github.com/yourusername/md5-hash-cracker.git

# Change directory to the project folder
cd md5-hash-cracker

# Ensure all dependencies are installed (if any)
pip install -r requirements.txt
```

**Note:** The above installation assumes the existence of a requirements file; if there are no external dependencies, this step can be omitted.

---

## Usage
To utilize the MD5 Hash Cracker, execute the following command in your terminal:

```bash
python hash_cracker.py
```

### Input Format
- The program will prompt you to **Enter the Hash to Crack**. Provide the MD5 hash you wish to reverse.

### Output
- Upon execution, the program will output either:
  - `Successfully Cracked Password: [password]` if a matching plaintext password is found.
  - `Hash Not Cracked` if no matches are found after examining all entries in the provided password list.

---

## Code Explanation
The following Python code illustrates the logic behind the MD5 Hash Cracker:

```python
import hashlib  # Importing the hashlib module to access hashing functions

# Prompt user for input
hash_to_crack = input("Enter the Hash to Crack: ").strip()

# Open password list file
with open('passwords.txt', 'r') as f:
    # Iterate over each line in the file
    for line in f:
        password = line.strip()  # Strip any extraneous whitespace/newline
        encrypted_password = hashlib.md5(password.encode()).hexdigest()  # Hash the current password
        
        if hash_to_crack == encrypted_password:  # Check for a match
            print(f"Successfully Cracked Password: {password}")  # Output result
            break  # Exit loop if a match is found
    else:
        # Executed only if no break occurs
        print("Hash Not Cracked")  # Indicate failure to crack the hash
```

---

## Detailed Breakdown
- **Module Import**: The `hashlib` module is imported to facilitate hashing functions, specifically for MD5 hashing.
- **Input Handling**: The user is prompted to input the hash they wish to crack, which is stripped of surrounding whitespace.
- **File Handling**: The password file is opened, and each line is processed sequentially:
  - Each password is stripped of whitespace and hashed using MD5.
  - The hashed password is compared to the user-provided hash.
- **Match Handling**: If a match is found, the corresponding password is printed, and the loop terminates. If no matches are found after checking all passwords, a failure message is displayed.

---

## Contributing
Contributions to enhance the functionality or efficiency of this script are welcome. Please fork the repository, make your modifications, and submit a pull request for review.

---

## License
This project is licensed under the GNU License. See the [LICENSE](LICENSE) file for details.

---
