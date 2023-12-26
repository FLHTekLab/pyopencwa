from bs4 import BeautifulSoup
import os

# 讀取 HTML 文件
file_path = 'cwa-opendata-api-spec.html'

with open(file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

# 使用 BeautifulSoup 解析 HTML
soup = BeautifulSoup(html_content, 'html.parser')

# 找到所有 class 為 'opblock-tag-section' 的 div 元素
div_elements = soup.find_all('div', class_='opblock-tag-section')
files = []
for div in div_elements:
    # 找到每個 div 內部的 h3 元素，並取得其內部文本作為文件名
    h3 = div.find('h3', class_='opblock-tag')
    if h3:
        file_name = h3.get_text(strip=True).replace('/', '_') + '.html'
        file_path = os.path.join('.', file_name)
        files.append(file_name)

        # 將 div 元素的 HTML 內容寫入到文件
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(str(div))
            print(f"save {file_path}")

print(f"{files}")
