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

    param_classes = set()

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
            api_summary = founds[0].text.strip()

            apis[api_type].append({
                "path": api_path,
                "summary": api_summary
            })

        
        # 假設 `div` 是你從 `<table class="parameters">` 中找到的 div
        # tables = section.find_all("table", class_="parameters")
        # assert len(tables) >= 1
        # for t in tables:
        #     founds = t.find_all("div")
        #     for f in founds:
        #         param_classes.add(f.get("class")[0])
        # """
        # {'parameter__enum', 'parameter__type', 'parameter__in', 'parameter__deprecated', 'parameter__name', 'json-schema-array', 'markdown'}
        # """

        # api_description <div class="opblock-description">
        # api_parameters <table class="parameters">
        # api_parameter <tr>
        # param <td class="parameters-col_name">
        # param_field <div class="parameter__name required">
        # param_field <div class="parameter__type">
        # param_field <div class="parameter__deprecated">
        # param_field <div class="parameter__in">
        """
        <td class="parameters-col_name">
        <div class="parameter__name required">Authorization<span>&nbsp;*</span></div>
        <div class="parameter__type">string</div>
        <div class="parameter__deprecated"></div>
        <div class="parameter__in">(query)</div>
        </td>"""



        # 注意：div.get('class') 會回傳一個 list，因為一個元素可以有多個 class。如果你知道每個 div 只有一個 class，你可以使用 div.get('class')[0] 來取得該 class。如果一個 div 可以有多個 class，你可能需要稍微修改上面的程式碼來處理這種情況。


print(param_classes)
# with open("cwa-opedata-api-spec.json", "w", encoding="utf-8") as file:
#     file.write(json.dumps(apis, indent=2, ensure_ascii=False))
# 這裡可以進行更多的處理，比如搜索特定的元素或提取特定的數據
