import tkinter as tk
from tkinter import messagebox

def submit_filename():
    filename = entry.get()
    if filename:
        messagebox.showinfo("文件名确认", f"您输入的文件名是: {filename}")
    else:
        messagebox.showwarning("输入错误", "请输入文件名")

# 创建主窗口
root = tk.Tk()
root.title("文件名输入")

# 创建提示标签
label = tk.Label(root, text="请输入文件名:")
label.pack(padx=10, pady=10)

# 创建输入框
entry = tk.Entry(root, width=40)
entry.pack(padx=10, pady=10)

# 创建提交按钮
submit_button = tk.Button(root, text="提交", command=submit_filename)
submit_button.pack(padx=10, pady=10)

# 运行主循环
root.mainloop()