"""
这个模块从指定网页抓取适合初学者的Python书籍信息，
根据书籍的销量进行排序，并将排序后的书籍信息保存到CSV文件中。
"""

# 导入所需的库
import requests
from bs4 import BeautifulSoup
import pandas as pd

# 发送HTTP请求获取网页内容
URL = 'https://ling017.github.io/Python-coursework/'
response = requests.get(URL, timeout=10)
response.raise_for_status()  # 检查请求是否成功

# 打印网页内容
print(response.text)

# 解析HTML内容
soup = BeautifulSoup(response.content, 'html.parser')

# 打印解析后的HTML内容
print(soup.prettify())

# 提取书籍信息
books = []
for book_item in soup.select('.book-item'):  # 假设书籍信息在class为book-item的元素中
    title = book_item.select_one('.title').get_text(strip=True)
    author = book_item.select_one('.author').get_text(strip=True)
    sales = int(book_item.select_one('.sales').get_text(strip=True).replace('销量: ', ''))
    print(f"Title: {title}, Author: {author}, Sales: {sales}")  # 打印提取到的书籍信息
    books.append({'title': title, 'author': author, 'sales': sales})

# 根据销量对书籍信息进行排序
sorted_books = sorted(books, key=lambda x: x['sales'], reverse=True)

# 将排序后的书籍信息保存为CSV文件
df = pd.DataFrame(sorted_books)
df.to_csv('sorted_books.csv', index=False, encoding='utf-8-sig')

print("书籍信息已成功抓取并保存到sorted_books.csv文件中。\n")
