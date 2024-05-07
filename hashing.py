import hashlib

def calculate_hash(file_path):
    # Read the file content and calculate SHA-256 hash
    with open(file_path, 'rb') as f:
        file_content = f.read()
        sha256_hash = hashlib.sha256(file_content).hexdigest()
    return sha256_hash

def verify_integrity(file_path, expected_hash):
    # Calculate hash of the file
    calculated_hash = calculate_hash(file_path)
    
    # Compare calculated hash with expected hash
    if calculated_hash == expected_hash:
        print("File integrity is valid.")
    else:
        print("File integrity verification failed.")

def main():
    print("1. Calculate the cryptographic hash of a file (SHA-256)")
    print("2. Verify the integrity of a file using the calculated hash")
    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        file_path = input("Enter the file path: ")
        sha256_hash = calculate_hash(file_path)
        print("SHA-256 hash of the file:", sha256_hash)
    elif choice == '2':
        file_path = input("Enter the file path: ")
        expected_hash = input("Enter the expected hash value: ")
        verify_integrity(file_path, expected_hash)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()



