import json
from bs4 import BeautifulSoup

# 假定您的 HTML 文件名為 'example.html'
file_path = "cwa-opendata-api-spec.html"

# 使用 with 語句打開文件，這樣可以確保文件在使用後會被正確關閉
with open(file_path, "r", encoding="utf-8") as file:
    # 讀取文件內容
    html_content = file.read()

    # json 儲存
    apis = {}

    # 使用 BeautifulSoup 解析 HTML 內容
    soup = BeautifulSoup(html_content, "html.parser")

    # 分析 html 內容中 API Section (div class="opblock-tag-section is-open")
    sections = soup.find_all("div", class_="opblock-tag-section is-open")

    for section in sections:
        # 找到所有的 h3 標籤，這是 API Section 的標題
        founds = section.find_all(["h3"])
        assert len(founds) == 1
        api_type = founds[0].text.strip()
        apis[api_type] = []


        # 找到所有的 div class="opblock-summary opblock-summary-get" 標籤，這是 每個 API Section 的內文
        divs = section.find_all("div", class_="opblock-summary opblock-summary-get")

        # 迭代每個 div，並打印其內容
        for div in divs:
            # 找到其中 span class="opblock-summary-path" 標籤，這是 API 的路徑
            founds = div.find_all("span", class_="opblock-summary-path")
            assert len(founds) == 1
            api_path = founds[0].text.strip()

            # 找到其中 div class="opblock-summary-description" 標籤，這是 API 的描述
            founds = div.find_all("div", class_="opblock-summary-description")
            assert len(founds) == 1
            api_description = founds[0].text.strip()
            
            apis[api_type].append({
                "path": api_path,
                "description": api_description
            })

with open("cwa-opedata-api-spec.json", "w", encoding="utf-8") as file:
    file.write(json.dumps(apis, indent=2, ensure_ascii=False))
# 這裡可以進行更多的處理，比如搜索特定的元素或提取特定的數據
