from cryptography.fernet import Fernet


class Crypt:

    def __init__(self):
        self.key = None

    def generate_key(self, filename="key"):
        """Take a filename to store the generated key"""

        self.key = Fernet.generate_key()

        with open('{}.key'.format(filename), 'wb') as filekey:
           filekey.write(self.key)

    def read_key(self, filename):
        """Take a file containing key and read the key"""

        with open(filename, 'rb') as filekey:
            self.key = filekey.read()

    def encrypt_file(self, filename, output_name):
        """Take a filename and encrypt it"""

        fernet = Fernet(self.key)

        with open(filename, 'rb') as file:
            original = file.read()

        encrypted = fernet.encrypt(original)

        with open(output_name, 'wb') as encrypted_file:
            encrypted_file.write(encrypted)

    def decrypt_file(self, filename, output_name):
        """Take an encrypted file and return the original page, decrypted"""

        fernet = Fernet(self.key)

        with open(filename, 'rb') as file:
            encrypted = file.read()

        decrypted = fernet.decrypt(encrypted)

        with open(output_name, 'wb') as file:
            file.write(decrypted)


if __name__ == '__main__':
    a = Crypt()



