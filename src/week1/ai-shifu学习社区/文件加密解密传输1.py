from cryptography.fernet import Fernet
import os

# 生成密钥并保存到文件
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

# 从文件中加载密钥
def load_key():
    return open("secret.key", "rb").read()

# 加密文件
def encrypt_file(file_path, key):
    fernet = Fernet(key)
    with open(file_path, "rb") as file:
        file_data = file.read()
    encrypted_data = fernet.encrypt(file_data)
    with open(file_path, "wb") as file:
        file.write(encrypted_data)
    print(f"文件 {file_path} 已加密")

# 解密文件
def decrypt_file(file_path, key):
    fernet = Fernet(key)
    with open(file_path, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = fernet.decrypt(encrypted_data)
    with open(file_path, "wb") as file:
        file.write(decrypted_data)
    print(f"文件 {file_path} 已解密")

# 主函数
def main():
    # 检查是否存在密钥文件，如果不存在则生成一个
    if not os.path.exists("secret.key"):
        generate_key()
    
    key = load_key()
    
    # 用户选择加密或解密
    choice = input("请选择操作 (1: 加密, 2: 解密): ")
    file_path = input("请输入文件路径: ")
    
    if choice == "1":
        encrypt_file(file_path, key)
    elif choice == "2":
        decrypt_file(file_path, key)
    else:
        print("无效的选择")

if __name__ == "__main__":
    main()