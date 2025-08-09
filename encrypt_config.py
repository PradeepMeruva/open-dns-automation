from cryptography.fernet import Fernet

# Generate a key and save it to a file
def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

# Encrypt the config file
def encrypt_config():
    with open("key.key", "rb") as key_file:
        key = key_file.read()
    fernet = Fernet(key)

    with open("config.json", "rb") as file:
        original = file.read()

    encrypted = fernet.encrypt(original)

    with open("config.json.encrypted", "wb") as encrypted_file:
        encrypted_file.write(encrypted)

if __name__ == "__main__":
    generate_key()
    encrypt_config()
    print("Config file encrypted and key generated.")