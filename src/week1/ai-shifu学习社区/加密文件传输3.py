
import tkinter as tk
from tkinter import filedialog
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
import base64
import os


def generate_key(password):
    # Generate encryption key from the password
    password_bytes = password.encode()
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=b'',
        iterations=100000,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password_bytes))
    return key


def encrypt_file(file_path, password):
    # Read the file content
    with open(file_path, 'rb') as file:
        file_content = file.read()

    # Generate encryption key from the password
    cipher_suite = Fernet(generate_key(password))

    # Encrypt the file content
    encrypted_content = cipher_suite.encrypt(file_content)

    # Modify the file name
    file_name = os.path.basename(file_path)
    encrypted_file_path = os.path.join(
        os.path.dirname(file_path), f"[已加密]目前未知")

    # Save the encrypted content to the new file
    with open(encrypted_file_path, 'wb') as encrypted_file:
        encrypted_file.write(encrypted_content)


def decrypt_file(file_path, password):
    # Read the encrypted file content
    with open(file_path, 'rb') as encrypted_file:
        encrypted_content = encrypted_file.read()

    # Generate encryption key from the password
    cipher_suite = Fernet(generate_key(password))

    # Decrypt the file content
    decrypted_content = cipher_suite.decrypt(encrypted_content)

    # Modify the file name
    file_name = os.path.basename(file_path)
    decrypted_file_path = os.path.join(
        os.path.dirname(file_path), f"[已解密]目前未知")

    # Save the decrypted content to the new file
    with open(decrypted_file_path, 'wb') as decrypted_file:
        decrypted_file.write(decrypted_content)


def select_file():
    # Open file dialog to select a file
    file_path = filedialog.askopenfilename()

    # Perform encryption on the selected file
    encrypt_file(file_path, password_entry.get())


def select_encrypted_file():
    # Open file dialog to select an encrypted file
    file_path = filedialog.askopenfilename()

    # Perform decryption on the selected file
    decrypt_file(file_path, password_entry.get())


# Create the GUI window
window = tk.Tk()
window.title("File Encryption/Decryption")
window.geometry("300x150")

# Create the password input field
password_label = tk.Label(window, text="Password:")
password_label.pack()
password_entry = tk.Entry(window, show="*")
password_entry.pack()

# Create the "Encrypt" button
encrypt_button = tk.Button(window, text="Encrypt", command=select_file)
encrypt_button.pack(side=tk.LEFT)

# Create the "Decrypt" button
decrypt_button = tk.Button(window, text="Decrypt",
                           command=select_encrypted_file)
decrypt_button.pack(side=tk.RIGHT)

# Start the GUI event loop
window.mainloop()
