"""
設計一個以 cwa_rest_api_dict.py 檔案內 CWA_REST_API_DICT nested dict 物件為基礎，
並以 click package 中 click.MultiCommand 所設計的 python script command line tool (cli)，
這個 cli 工具的 click.MultiCommand help 參數為"中央氣象署開放資料平臺之資料擷取API"
CWA_REST_API_DICT 的資料結構如下
{
    "groupCmd":{
        "title": "groupCmdTxt",
        ...,
        "apis": [
            "dataId": "subCmdTxt",
            "summary": "subCmdHelp",
            ...
        ],
    }
}
對應的 group cmd help string 是為所對應的 value dict["title"]，
每個 group cmd 對應的 sub cmd 是所對應的 dataId string
每個 sub-cmd help string 為對應的 subCmdHelp string
"""
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
    group_cmd_txt = title = f"{filename.replace('.html', '')}"
    if title == '預報':
        group_cmd_txt = 'forecast'
    elif title == '觀測':
        group_cmd_txt = 'observation'
    elif title == '地震海嘯':
        group_cmd_txt = 'earthquake'
    elif title == '氣候':
        group_cmd_txt = 'climate'
    elif title == '天氣警特報':
        group_cmd_txt = 'alert'
    elif title == '數值預報':
        group_cmd_txt = 'health'
    elif title == '天文':
        group_cmd_txt = 'astronomy'
    else:
        raise NotImplementedError

    apis = []
    group_cmd = {
        "cmd": group_cmd_txt,
        "title": title,
        "apis": apis
    }
    sections[group_cmd_txt] = group_cmd
    for block in api_blocks:
        api = {
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

with open('cwa-rest-api-dict.json', 'w', encoding='utf-8') as file:
    file.write(json.dumps(sections, indent=2, ensure_ascii=False))
