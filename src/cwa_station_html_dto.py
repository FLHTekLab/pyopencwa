from bs4 import BeautifulSoup
import json

# 讀取 HTML 文件
file_path = 'cwa-station-state.html'

with open(file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

# 使用 BeautifulSoup 解析 HTML
soup = BeautifulSoup(html_content, 'html.parser')

# 找到 class 為 'existing_station' 的 div 元素
founds = soup.find_all('div', id='existing_station')
assert len(founds) == 1
existing_station_div = founds[0]

# 提取表格
table = existing_station_div.find('table')

# 解析表格
data = []
headers = [th.get_text(strip=True) for th in table.find_all('th')]

# 遍歷每一行
for row in table.find_all('tr')[1:]:  # Skip the header row
    cells = row.find_all('td')
    row_data = dict(zip(headers, [cell.get_text(strip=True) for cell in cells]))
    data.append(row_data)

# 顯示或保存 JSON 數據
with open('cwa-station-state.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, indent=2, ensure_ascii=False)
