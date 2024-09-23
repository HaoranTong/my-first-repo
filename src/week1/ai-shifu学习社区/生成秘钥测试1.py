import os
from tkinter import Tk, Label, Entry, Button, filedialog, messagebox
from cryptography.fernet import Fernet

def generate_key():
    """生成密钥"""
    return Fernet.generate_key()

def encrypt_file(file_path, password):
    """加密文件"""
    key = generate_key()
    fernet = Fernet(key)
    with open(file_path, "rb") as file:
        file_data = file.read()
    encrypted_data = fernet.encrypt(file_data)
    encrypted_file_path = os.path.join(os.path.dirname(file_path), "[已加密]" + os.path.basename(file_path))
    with open(encrypted_file_path, "wb") as file:
        file.write(encrypted_data)
    messagebox.showinfo("成功", f"文件已加密并保存为: {encrypted_file_path}")

def decrypt_file(file_path, password):
    """解密文件"""
    key = generate_key()
    fernet = Fernet(key)
    with open(file_path, "rb") as file:
        encrypted_data = file.read()
    try:
        decrypted_data = fernet.decrypt(encrypted_data)
        decrypted_file_path = os.path.join(os.path.dirname(file_path), "[已解密]" + os.path.basename(file_path))
        with open(decrypted_file_path, "wb") as file:
            file.write(decrypted_data)
        messagebox.showinfo("成功", f"文件已解密并保存为: {decrypted_file_path}")
    except cryptography.fernet.InvalidToken:
        messagebox.showerror("错误", "解密失败，请检查密码是否正确")

def select_file_encrypt():
    """选择文件并加密"""
    file_path = filedialog.askopenfilename()
    if file_path:
        password = password_entry.get()
        if password:
            encrypt_file(file_path, password)
        else:
            messagebox.showwarning("警告", "请输入密码")

def select_file_decrypt():
    """选择文件并解密"""
    file_path = filedialog.askopenfilename()
    if file_path:
        password = password_entry.get()
        if password:
            decrypt_file(file_path, password)
        else:
            messagebox.showwarning("警告", "请输入密码")

# 创建主窗口
root = Tk()
root.title("文件加密解密工具")

# 创建密码输入框
Label(root, text="请输入密码:").grid(row=0, column=0, padx=10, pady=10)
password_entry = Entry(root, show="*")
password_entry.grid(row=0, column=1, padx=10, pady=10)

# 创建加密和解密按钮
encrypt_button = Button(root, text="选择文件并加密", command=select_file_encrypt)
encrypt_button.grid(row=1, column=0, padx=10, pady=10)

decrypt_button = Button(root, text="选择文件并解密", command=select_file_decrypt)
decrypt_button.grid(row=1, column=1, padx=10, pady=10)

# 运行主循环
root.mainloop()