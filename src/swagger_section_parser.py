from bs4 import BeautifulSoup
import json

filenames = ['預報.html', '觀測.html', '地震海嘯.html', '氣候.html', '天氣警特報.html', '數值預報.html', '天文.html']
sections = {}

for filename in filenames:
    # 假定 html_content 包含您的 HTML 內容
    with open(f'{filename}') as fh:
        html_content = fh.read()

    # 使用 BeautifulSoup 解析 HTML
    soup = BeautifulSoup(html_content, 'lxml')

    # 找到所有的 API 塊
    api_blocks = soup.find_all("div", class_="opblock opblock-get is-open")

    # 解析並提取所需的信息
    cmd = title = f"{filename.replace('.html', '')}"
    if title == '預報':
        cmd = 'forecast'
    elif title == '觀測':
        cmd = 'observation'
    elif title == '地震海嘯':
        cmd = 'earthquake'
    elif title == '氣候':
        cmd = 'climate'
    elif title == '天氣警特報':
        cmd = 'alert'
    elif title == '數值預報':
        cmd = 'numerical_forecast'
    elif title == '天文':
        cmd = 'astronomy'
    else:
        raise NotImplementedError

    sections[cmd] = apis = []
    for block in api_blocks:
        api = {
            'title': title,
            'cmd': cmd,
            'path': block.find("span", class_="opblock-summary-path").get_text(strip=True),
            'dataId': block.find("span", class_="opblock-summary-path").get_text(strip=True).split('/')[-1],
            'summary': block.find("div", class_="opblock-summary-description").get_text(strip=True),
            'description': block.find("div", class_="opblock-description").get_text(strip=True),
        }

        # 提取 API 參數
        parameters = []
        params_table = block.find("table", class_="parameters")
        if params_table:
            for row in params_table.find_all("tr")[1:]:  # Skip header row
                param = {}
                name_col, desc_col = row.find_all("td")
                param['name'] = name_col.find("div", class_="parameter__name").get_text(strip=True).replace('*', '')
                param['required'] = 'required' in name_col.find("div", class_="parameter__name").get('class', [])
                param['type'] = name_col.find("div", class_="parameter__type").get_text(strip=True)
                param['description'] = desc_col.get_text(strip=True)
                parameters.append(param)

        api['parameters'] = parameters
        apis.append(api)

with open('cwa-opendata-api-spec.json', 'w', encoding='utf-8') as file:
    file.write(json.dumps(sections, indent=2, ensure_ascii=False))
