CWA_REST_API_DICT={
  "forecast": {
    "cmd": "forecast",
    "title": "預報",
    "apis": [
      {
        "path": "/v1/rest/datastore/F-C0032-001",
        "dataId": "F-C0032-001",
        "summary": "一般天氣預報-今明 36 小時天氣預報",
        "description": "臺灣各縣市天氣預報資料及國際都市天氣預報",
        "parameters": [
          {
            "name": "Authorization",
            "required": True,
            "type": "string",
            "description": "氣象開放資料平台會員授權碼"
          },
          {
            "name": "limit",
            "required": False,
            "type": "number($int)",
            "description": "限制最多回傳的資料，預設為回傳全部筆數"
          },
          {
            "name": "offset",
            "required": False,
            "type": "number($int)",
            "description": "指定從第幾筆後開始回傳，預設為第 0 筆開始回傳"
          },
          {
            "name": "format",
            "required": False,
            "type": "string",
            "description": "回傳資料格式，預設為 json 格式Available values: JSON, XML--JSONXML"
          },
          {
            "name": "locationName",
            "required": False,
            "type": "array[string]",
            "description": "臺灣各縣市，預設為回傳全部縣市Available values: 宜蘭縣, 花蓮縣, 臺東縣, 澎湖縣, 金門縣, 連江縣, 臺北市, 新北市, 桃園市, 臺中市, 臺南市, 高雄市, 基隆市, 新竹縣, 新竹市, 苗栗縣, 彰化縣, 南投縣, 雲林縣, 嘉義縣, 嘉義市, 屏東縣--宜蘭縣花蓮縣臺東縣澎湖縣金門縣連江縣臺北市新北市桃園市臺中市臺南市高雄市基隆市新竹縣新竹市苗栗縣彰化縣南投縣雲林縣嘉義縣嘉義市屏東縣"
          },
          {
            "name": "elementName",
            "required": False,
            "type": "array[string]",
            "description": "天氣因子，預設為全部回傳Available values: Wx, PoP, CI, MinT, MaxT--WxPoPCIMinTMaxT"
          },
          {
            "name": "sort",
            "required": False,
            "type": "string",
            "description": "同時對 「startTime」，「endTime」 做升冪排序，預設不排序Available values: time--time"
          },
          {
            "name": "startTime",
            "required": False,
            "type": "array[string]",
            "description": "時間因子，格式為「yyyy-MM-ddThh:mm:ss」，預設為全部回傳"
          },
          {
            "name": "timeFrom",
            "required": False,
            "type": "string($date-time)",
            "description": "時間區段，篩選需要之時間區段，時間從「timeFrom」 開始篩選，直到內容之最後時間，並可與參數 「timeTo」 合併使用，格式為「yyyy-MM-ddThh:mm:ss」，若使用參數「startTime」，則參數「timeFrom」的篩選資料則會失去作用， 預設為全部回傳"
          },
          {
            "name": "timeTo",
            "required": False,
            "type": "string($date-time)",
            "description": "時間區段，根據內容可篩選需要之時間區段，時間從內容之最初時間開始篩選，直到 「timeTo」，並可與參數 「timeFrom」 合併使用，格式為「yyyy-MM-ddThh:mm:ss」，若使用「startTime」，則參數「timeTo」的篩選資料則會失效，預設為全部回傳"
          }
        ]
      },
      {
        "path": "/v1/rest/datastore/F-D0047-001",
        "dataId": "F-D0047-001",
        "summary": "鄉鎮天氣預報-宜蘭縣未來2天天氣預報",
        "description": "臺灣各鄉鎮市區預報資料-臺灣各鄉鎮市區未來2天(逐3小時)及未來1週天氣預報",
        "parameters": [
          {
            "name": "Authorization",
            "required": True,
            "type": "string",
            "description": "氣象開放資料平台會員授權碼"
          },
          {
            "name": "limit",
            "required": False,
            "type": "number($int)",
            "description": "限制最多回傳的資料，預設為回傳全部筆數"
          },
          {
            "name": "offset",
            "required": False,
            "type": "number($int)",
            "description": "指定從第幾筆後開始回傳，預設為第 0 筆開始回傳"
          },
          {
            "name": "format",
            "required": False,
            "type": "string",
            "description": "回傳資料格式，預設為 json 格式Available values: JSON, XML--JSONXML"
          },
          {
            "name": "locationName",
            "required": False,
            "type": "array[string]",
            "description": "各縣市所對應鄉鎮名稱，請參考https://opendata.cwa.gov.tw/opendatadoc/Opendata_City.pdf，附錄 A『全臺縣市鄉鎮對照表』，預設為全部回傳"
          },
          {
            "name": "elementName",
            "required": False,
            "type": "array[string]",
            "description": "天氣預報因子，預設為全部回傳Available values: Wx, PoP12h, AT, T, RH, CI, WeatherDescription, PoP6h, WS, WD, Td--WxPoP12hATTRHCIWeatherDescriptionPoP6hWSWDTd"
          },
          {
            "name": "sort",
            "required": False,
            "type": "string",
            "description": "同時對 「startTime」，「endTime」，「dataTime」 做升冪排序，預設不排序Available values: time--time"
          },
          {
            "name": "startTime",
            "required": False,
            "type": "array[string]",
            "description": "時間因子，格式為「yyyy-MM-ddThh:mm:ss」，預設為全部回傳"
          },
          {
            "name": "dataTime",
            "required": False,
            "type": "array[string]",
            "description": "時間因子，格式為「yyyy-MM-ddThh:mm:ss」，預設為全部回傳"
          },
          {
            "name": "timeFrom",
            "required": False,
            "type": "string($date-time)",
            "description": "時間區段:時間從「timeFrom」 開始篩選，直到內容之最後時間，並可與參數 「timeTo 合併使用，格式為「yyyy-MM-ddThh:mm:ss」， 若使用參數「startTime」或「dataTime」，則參數「timeFrom」的篩選資料則會失效，預設為全部回傳"
          },
          {
            "name": "timeTo",
            "required": False,
            "type": "string($date-time)",
            "description": "時間區段，篩選需要之時間區段，時間從內容之最初時間開始篩選，直到 「timeTo」，並可與參數 「timeFrom」 合併使用，格式為「yyyy-MM-ddThh:mm:ss」，使用「startTime」或「dataTime」，則參數「timeTo」的篩選資料則會失效，預設為全部回傳"
          }
        ]
      },
      {
        "path": "/v1/rest/datastore/F-D0047-003",
        "dataId": "F-D0047-003",
        "summary": "鄉鎮天氣預報-宜蘭縣未來1週天氣預報",
        "description": "臺灣各鄉鎮市區預報資料-臺灣各鄉鎮市區未來2天(逐3小時)及未來1週天氣預報",
        "parameters": [
          {
            "name": "Authorization",
            "required": True,
            "type": "string",
            "description": "氣象開放資料平台會員授權碼"
          },
          {
            "name": "limit",
            "required": False,
            "type": "number($int)",
            "description": "限制最多回傳的資料，預設為回傳全部筆數"
          },
          {
            "name": "offset",
            "required": False,
            "type": "number($int)",
            "description": "指定從第幾筆後開始回傳，預設為第 0 筆開始回傳"
          },
          {
            "name": "format",
            "required": False,
            "type": "string",
            "description": "回傳資料格式，預設為 json 格式Available values: JSON, XML--JSONXML"
          },
          {
            "name": "locationName",
            "required": False,
            "type": "array[string]",
            "description": "各縣市所對應鄉鎮名稱，請參考https://opendata.cwa.gov.tw/opendatadoc/Opendata_City.pdf，附錄 A『全臺縣市鄉鎮對照表』，預設為全部回傳"
          },
          {
            "name": "elementName",
            "required": False,
            "type": "array[string]",
            "description": "天氣預報因子，預設為全部回傳Available values: MinCI, MaxAT, MaxCI, MinT, UVI, MinAT, MaxT, Wind, Td, PoP12h, T, RH, Wx, WeatherDescription--MinCIMaxATMaxCIMinTUVIMinATMaxTWindTdPoP12hTRHWxWeatherDescription"
          },
          {
            "name": "sort",
            "required": False,
            "type": "string",
            "description": "同時對 「startTime」，「endTime」，「dataTime」 做升冪排序，預設不排序Available values: time--time"
          },
          {
            "name": "startTime",
            "required": False,
            "type": "array[string]",
            "description": "時間因子，格式為「yyyy-MM-ddThh:mm:ss」，預設為全部回傳"
          },
          {
            "name": "dataTime",
            "required": False,
            "type": "array[string]",
            "description": "時間因子，格式為「yyyy-MM-ddThh:mm:ss」，預設為全部回傳"
          },
          {
            "name": "timeFrom",
            "required": False,
            "type": "string($date-time)",
            "description": "時間區段:時間從「timeFrom」 開始篩選，直到內容之最後時間，並可與參數 「timeTo」 合併使用，格式為「yyyy-MM-ddThh:mm:ss」， 若使用參數「startTime」或「dataTime」，則參數「timeFrom」的篩選資料則會失效，預設為全部回傳"
          },
          {
            "name": "timeTo",
            "required": False,
            "type": "string($date-time)",
            "description": "時間區段，篩選需要之時間區段，時間從內容之最初時間開始篩選，直到 「timeTo」，並可與參數 「timeFrom」 合併使用，格式為「yyyy-MM-ddThh:mm:ss」，使用「startTime」或「dataTime」，則參數「timeTo」的篩選資料則會失效，預設為全部回傳"
          }
        ]
      },
      {
        "path": "/v1/rest/datastore/F-D0047-005",
        "dataId": "F-D0047-005",
        "summary": "鄉鎮天氣預報-桃園市未來2天天氣預報",
        "description": "臺灣各鄉鎮市區預報資料-臺灣各鄉鎮市區未來2天(逐3小時)及未來1週天氣預報",
        "parameters": [
          {
            "name": "Authorization",
            "required": True,
            "type": "string",
            "description": "氣象開放資料平台會員授權碼"
          },
          {
            "name": "limit",
            "required": False,
            "type": "number($int)",
            "description": "限制最多回傳的資料，預設為回傳全部筆數"
          },
          {
            "name": "offset",
            "required": False,
            "type": "number($int)",
            "description": "指定從第幾筆後開始回傳，預設為第 0 筆開始回傳"
          },
          {
            "name": "format",
            "required": False,
            "type": "string",
            "description": "回傳資料格式，預設為 json 格式Available values: JSON, XML--JSONXML"
          },
          {
            "name": "locationName",
            "required": False,
            "type": "array[string]",
            "description": "各縣市所對應鄉鎮名稱，請參考https://opendata.cwa.gov.tw/opendatadoc/Opendata_City.pdf，附錄 A『全臺縣市鄉鎮對照表』，預設為全部回傳"
          },
          {
            "name": "elementName",
            "required": False,
            "type": "array[string]",
            "description": "天氣預報因子，預設為全部回傳Available values: Wx, PoP12h, AT, T, RH, CI, WeatherDescription, PoP6h, WS, WD, Td--WxPoP12hATTRHCIWeatherDescriptionPoP6hWSWDTd"
          },
          {
            "name": "sort",
            "required": False,
            "type": "string",
            "description": "同時對 「startTime」，「endTime」，「dataTime」 做升冪排序，預設不排序Available values: time--time"
          },
          {
            "name": "startTime",
            "required": False,
            "type": "array[string]",
            "description": "時間因子，格式為「yyyy-MM-ddThh:mm:ss」，預設為全部回傳"
          },
          {
            "name": "dataTime",
            "required": False,
            "type": "array[string]",
            "description": "時間因子，格式為「yyyy-MM-ddThh:mm:ss」，預設為全部回傳"
          },
          {
            "name": "timeFrom",
            "required": False,
            "type": "string($date-time)",
            "description": "時間區段:時間從「timeFrom」 開始篩選，直到內容之最後時間，並可與參數 「timeTo 合併使用，格式為「yyyy-MM-ddThh:mm:ss」， 若使用參數「startTime」或「dataTime」，則參數「timeFrom」的篩選資料則會失效，預設為全部回傳"
          },
          {
            "name": "timeTo",
            "required": False,
            "type": "string($date-time)",
            "description": "時間區段，篩選需要之時間區段，時間從內容之最初時間開始篩選，直到 「timeTo」，並可與參數 「timeFrom」 合併使用，格式為「yyyy-MM-ddThh:mm:ss」，使用「startTime」或「dataTime」，則參數「timeTo」的篩選資料則會失效，預設為全部回傳"
          }
        ]
      },
      {
        "path": "/v1/rest/datastore/F-D0047-007",
        "dataId": "F-D0047-007",
        "summary": "鄉鎮天氣預報-桃園市未來1週天氣預報",
        "description": "臺灣各鄉鎮市區預報資料-臺灣各鄉鎮市區未來2天(逐3小時)及未來1週天氣預報",
        "parameters": [
          {
            "name": "Authorization",
            "required": True,
            "type": "string",
            "description": "氣象開放資料平台會員授權碼"
          },
          {
            "name": "limit",
            "required": False,
            "type": "number($int)",
            "description": "限制最多回傳的資料，預設為回傳全部筆數"
          },
          {
            "name": "offset",
            "required": False,
            "type": "number($int)",
            "description": "指定從第幾筆後開始回傳，預設為第 0 筆開始回傳"
          },
          {
            "name": "format",
            "required": False,
            "type": "string",
            "description": "回傳資料格式，預設為 json 格式Available values: JSON, XML--JSONXML"
          },
          {
            "name": "locationName",
            "required": False,
            "type": "array[string]",
            "description": "各縣市所對應鄉鎮名稱，請參考https://opendata.cwa.gov.tw/opendatadoc/Opendata_City.pdf，附錄 A『全臺縣市鄉鎮對照表』，預設為全部回傳"
          },
          {
            "name": "elementName",
            "required": False,
            "type": "array[string]",
            "description": "天氣預報因子，預設為全部回傳Available values: MinCI, MaxAT, MaxCI, MinT, UVI, MinAT, MaxT, WS, WD, Td, PoP12h, T, RH, Wx, WeatherDescription--MinCIMaxATMaxCIMinTUVIMinATMaxTWSWDTdPoP12hTRHWxWeatherDescription"
          },
          {
            "name": "sort",
            "required": False,
            "type": "string",
            "description": "同時對 「startTime」，「endTime」，「dataTime」 做升冪排序，預設不排序Available values: time--time"
          },
          {
            "name": "startTime",
            "required": False,
            "type": "array[string]",
            "description": "時間因子，格式為「yyyy-MM-ddThh:mm:ss」，預設為全部回傳"
          },
          {
            "name": "dataTime",
            "required": False,
            "type": "array[string]",
            "description": "時間因子，格式為「yyyy-MM-ddThh:mm:ss」，預設為全部回傳"
          },
          {
            "name": "timeFrom",
            "required": False,
            "type": "string($date-time)",
            "description": "時間區段:時間從「timeFrom」 開始篩選，直到內容之最後時間，並可與參數 「timeTo 合併使用，格式為「yyyy-MM-ddThh:mm:ss」， 若使用參數「startTime」或「dataTime」，則參數「timeFrom」的篩選資料則會失效，預設為全部回傳"
          },
          {
            "name": "timeTo",
            "required": False,
            "type": "string($date-time)",
            "description": "時間區段，篩選需要之時間區段，時間從內容之最初時間開始篩選，直到 「timeTo」，並可與參數 「timeFrom」 合併使用，格式為「yyyy-MM-ddThh:mm:ss」，使用「startTime」或「dataTime」，則參數「timeTo」的篩選資料則會失效，預設為全部回傳"
          }
        ]
      },
      {
        "path": "/v1/rest/datastore/F-D0047-009",
        "dataId": "F-D0047-009",
        "summary": "鄉鎮天氣預報-新竹縣未來2天天氣預報",
        "description": "臺灣各鄉鎮市區預報資料-臺灣各鄉鎮市區未來2天(逐3小時)及未來1週天氣預報",
        "parameters": [
          {
            "name": "Authorization",
            "required": True,
            "type": "string",
            "description": "氣象開放資料平台會員授權碼"
          },
          {
            "name": "limit",
            "required": False,
            "type": "number($int)",
            "description": "限制最多回傳的資料，預設為回傳全部筆數"
          },
          {
            "name": "offset",
            "required": False,
            "type": "number($int)",
            "description": "指定從第幾筆後開始回傳，預設為第 0 筆開始回傳"
          },
          {
            "name": "format",
            "required": False,
            "type": "string",
            "description": "回傳資料格式，預設為 json 格式Available values: JSON, XML--JSONXML"
          },
          {
            "name": "locationName",
            "required": False,
            "type": "array[string]",
            "description": "各縣市所對應鄉鎮名稱，請參考https://opendata.cwa.gov.tw/opendatadoc/Opendata_City.pdf，附錄 A『全臺縣市鄉鎮對照表』，預設為全部回傳"
          },
          {
            "name": "elementName",
            "required": False,
            "type": "array[string]",
            "description": "天氣預報因子，預設為全部回傳Available values: Wx, PoP12h, AT, T, RH, CI, WeatherDescription, PoP6h, WS, WD, Td--WxPoP12hATTRHCIWeatherDescriptionPoP6hWSWDTd"
          },
          {
            "name": "sort",
            "required": False,
            "type": "string",
            "description": "同時對 「startTime」，「endTime」，「dataTime」 做升冪排序，預設不排序Available values: time--time"
          },
          {
            "name": "startTime",
            "required": False,
            "type": "array[string]",
            "description": "時間因子，格式為「yyyy-MM-ddThh:mm:ss」，預設為全部回傳"
          },
          {
            "name": "dataTime",
            "required": False,
            "type": "array[string]",
            "description": "時間因子，格式為「yyyy-MM-ddThh:mm:ss」，預設為全部回傳"
          },
          {
            "name": "timeFrom",
            "required": False,
            "type": "string($date-time)",
            "description": "時間區段:時間從「timeFrom」 開始篩選，直到內容之最後時間，並可與參數 「timeTo 合併使用，格式為「yyyy-MM-ddThh:mm:ss」， 若使用參數「startTime」或「dataTime」，則參數「timeFrom」的篩選資料則會失效，預設為全部回傳"
          },
          {
            "name": "timeTo",
            "required": False,
            "type": "string($date-time)",
            "description": "時間區段，篩選需要之時間區段，時間從內容之最初時間開始篩選，直到 「timeTo」，並可與參數 「timeFrom」 合併使用，格式為「yyyy-MM-ddThh:mm:ss」，使用「startTime」或「dataTime」，則參數「timeTo」的篩選資料則會失效，預設為全部回傳"
          }
        ]
      },
      {
        "path": "/v1/rest/datastore/F-D0047-011",
        "dataId": "F-D0047-011",
        "summary": "鄉鎮天氣預報-新竹縣未來1週天氣預報",
        "description": "臺灣各鄉鎮市區預報資料-臺灣各鄉鎮市區未來2天(逐3小時)及未來1週天氣預報",
        "parameters": [
          {
            "name": "Authorization",
            "required": True,
            "type": "string",
            "description": "氣象開放資料平台會員授權碼"
          },
          {
            "name": "limit",
            "required": False,
            "type": "number($int)",
            "description": "限制最多回傳的資料，預設為回傳全部筆數"
          },
          {
            "name": "offset",
            "required": False,
            "type": "number($int)",
            "description": "指定從第幾筆後開始回傳，預設為第 0 筆開始回傳"
          },
          {
            "name": "format",
            "required": False,
            "type": "string",
            "description": "回傳資料格式，預設為 json 格式Available values: JSON, XML--JSONXML"
          },
          {
            "name": "locationName",
            "required": False,
            "type": "array[string]",
            "description": "各縣市所對應鄉鎮名稱，請參考https://opendata.cwa.gov.tw/opendatadoc/Opendata_City.pdf，附錄 A『全臺縣市鄉鎮對照表』，預設為全部回傳"
          },
          {
            "name": "elementName",
            "required": False,
            "type": "array[string]",
            "description": "天氣預報因子，預設為全部回傳Available values: MinCI, MaxAT, MaxCI, MinT, UVI, MinAT, MaxT, WS, WD, Td, PoP12h, T, RH, Wx, WeatherDescription--MinCIMaxATMaxCIMinTUVIMinATMaxTWSWDTdPoP12hTRHWxWeatherDescription"
          },
          {
            "name": "sort",
            "required": False,
            "type": "string",
            "description": "同時對 「startTime」，「endTime」，「dataTime」 做升冪排序，預設不排序Available values: time--time"
          },
          {
            "name": "startTime",
            "required": False,
            "type": "array[string]",
            "description": "時間因子，格式為「yyyy-MM-ddThh:mm:ss」，預設為全部回傳"
          },
          {
            "name": "dataTime",
            "required": False,
            "type": "array[string]",
            "description": "時間因子，格式為「yyyy-MM-ddThh:mm:ss」，預設為全部回傳"
          },
          {
            "name": "timeFrom",
            "required": False,
            "type": "string($date-time)",
            "description": "時間區段:時間從「timeFrom」 開始篩選，直到內容之最後時間，並可與參數 「timeTo 合併使用，格式為「yyyy-MM-ddThh:mm:ss」， 若使用參數「startTime」或「dataTime」，則參數「timeFrom」的篩選資料則會失效，預設為全部回傳"
          },
          {
            "name": "timeTo",
            "required": False,
            "type": "string($date-time)",
            "description": "時間區段，篩選需要之時間區段，時間從內容之最初時間開始篩選，直到 「timeTo」，並可與參數 「timeFrom」 合併使用，格式為「yyyy-MM-ddThh:mm:ss」，使用「startTime」或「dataTime」，則參數「timeTo」的篩選資料則會失效，預設為全部回傳"
          }
        ]
      },
      {
        "path": "/v1/rest/datastore/F-D0047-013",
        "dataId": "F-D0047-013",
        "summary": "鄉鎮天氣預報-苗栗縣未來2天天氣預報",
        "description": "臺灣各鄉鎮市區預報資料-臺灣各鄉鎮市區未來2天(逐3小時)及未來1週天氣預報",
        "parameters": [
          {
            "name": "Authorization",
            "required": True,
            "type": "string",
            "description": "氣象開放資料平台會員授權碼"
          },
          {
            "name": "limit",
            "required": False,
            "type": "number($int)",
            "description": "限制最多回傳的資料，預設為回傳全部筆數"
          },
          {
            "name": "offset",
            "required": False,
            "type": "number($int)",
            "description": "指定從第幾筆後開始回傳，預設為第 0 筆開始回傳"
          },
          {
            "name": "format",
            "required": False,
            "type": "string",
            "description": "回傳資料格式，預設為 json 格式Available values: JSON, XML--JSONXML"
          },
          {
            "name": "locationName",
            "required": False,
            "type": "array[string]",
            "description": "各縣市所對應鄉鎮名稱，請參考https://opendata.cwa.gov.tw/opendatadoc/Opendata_City.pdf，附錄 A『全臺縣市鄉鎮對照表』，預設為全部回傳"
          },
          {
            "name": "elementName",
            "required": False,
            "type": "array[string]",
            "description": "天氣預報因子，預設為全部回傳Available values: Wx, PoP12h, AT, T, RH, CI, WeatherDescription, PoP6h, WS, WD, Td--WxPoP12hATTRHCIWeatherDescriptionPoP6hWSWDTd"
          },
          {
            "name": "sort",
            "required": False,
            "type": "string",
            "description": "同時對 「startTime」，「endTime」，「dataTime」 做升冪排序，預設不排序Available values: time--time"
          },
          {
            "name": "startTime",
            "required": False,
            "type": "array[string]",
            "description": "時間因子，格式為「yyyy-MM-ddThh:mm:ss」，預設為全部回傳"
          },
          {
            "name": "dataTime",
            "required": False,
            "type": "array[string]",
            "description": "時間因子，格式為「yyyy-MM-ddThh:mm:ss」，預設為全部回傳"
          },
          {
            "name": "timeFrom",
            "required": False,
            "type": "string($date-time)",
            "description": "時間區段:時間從「timeFrom」 開始篩選，直到內容之最後時間，並可與參數 「timeTo 合併使用，格式為「yyyy-MM-ddThh:mm:ss」， 若使用參數「startTime」或「dataTime」，則參數「timeFrom」的篩選資料則會失效，預設為全部回傳"
          },
          {
            "name": "timeTo",
            "required": False,
            "type": "string($date-time)",
            "description": "時間區段，篩選需要之時間區段，時間從內容之最初時間開始篩選，直到 「timeTo」，並可與參數 「timeFrom」 合併使用，格式為「yyyy-MM-ddThh:mm:ss」，使用「startTime」或「dataTime」，則參數「timeTo」的篩選資料則會失效，預設為全部回傳"
          }
        ]
      },
      {
        "path": "/v1/rest/datastore/F-D0047-015",
        "dataId": "F-D0047-015",
        "summary": "鄉鎮天氣預報-苗栗縣未來1週天氣預報",
        "description": "臺灣各鄉鎮市區預報資料-臺灣各鄉鎮市區未來2天(逐3小時)及未來1週天氣預報",
        "parameters": [
          {
            "name": "Authorization",
            "required": True,
            "type": "string",
            "description": "氣象開放資料平台會員授權碼"
          },
          {
            "name": "limit",
            "required": False,
            "type": "number($int)",
            "description": "限制最多回傳的資料，預設為回傳全部筆數"
          },
          {
            "name": "offset",
            "required": False,
            "type": "number($int)",
            "description": "指定從第幾筆後開始回傳，預設為第 0 筆開始回傳"
          },
          {
            "name": "format",
            "required": False,
            "type": "string",
            "description": "回傳資料格式，預設為 json 格式Available values: JSON, XML--JSONXML"
          },
          {
            "name": "locationName",
            "required": False,
            "type": "array[string]",
            "description": "各縣市所對應鄉鎮名稱，請參考https://opendata.cwa.gov.tw/opendatadoc/Opendata_City.pdf，附錄 A『全臺縣市鄉鎮對照表』，預設為全部回傳"
          },
          {
            "name": "elementName",
            "required": False,
            "type": "array[string]",
            "description": "天氣預報因子，預設為全部回傳Available values: MinCI, MaxAT, MaxCI, MinT, UVI, MinAT, MaxT, WS, WD, Td, PoP12h, T, RH, Wx, WeatherDescription--MinCIMaxATMaxCIMinTUVIMinATMaxTWSWDTdPoP12hTRHWxWeatherDescription"
          },
          {
            "name": "sort",
            "required": False,
            "type": "string",
            "description": "同時對 「startTime」，「endTime」，「dataTime」 做升冪排序，預設不排序Available values: time--time"
          },
          {
            "name": "startTime",
            "required": False,
            "type": "array[string]",
            "description": "時間因子，格式為「yyyy-MM-ddThh:mm:ss」，預設為全部回傳"
          },
          {
            "name": "dataTime",
            "required": False,
            "type": "array[string]",
            "description": "時間因子，格式為「yyyy-MM-ddThh:mm:ss」，預設為全部回傳"
          },
          {
            "name": "timeFrom",
            "required": False,
            "type": "string($date-time)",
            "description": "時間區段:時間從「timeFrom」 開始篩選，直到內容之最後時間，並可與參數 「timeTo 合併使用，格式為「yyyy-MM-ddThh:mm:ss」， 若使用參數「startTime」或「dataTime」，則參數「timeFrom」的篩選資料則會失效，預設為全部回傳"
          },
          {
            "name": "timeTo",
            "required": False,
            "type": "string($date-time)",
            "description": "時間區段，篩選需要之時間區段，時間從內容之最初時間開始篩選，直到 「timeTo」，並可與參數 「timeFrom」 合併使用，格式為「yyyy-MM-ddThh:mm:ss」，使用「startTime」或「dataTime」，則參數「timeTo」的篩選資料則會失效，預設為全部回傳"
          }
        ]
      },
      {
        "path": "/v1/rest/datastore/F-D0047-017",
        "dataId": "F-D0047-017",
        "summary": "鄉鎮天氣預報-彰化縣未來2天天氣預報",
        "description": "臺灣各鄉鎮市區預報資料-臺灣各鄉鎮市區未來2天(逐3小時)及未來1週天氣預報",
        "parameters": [
          {
            "name": "Authorization",
            "required": True,
            "type": "string",
            "description": "氣象開放資料平台會員授權碼"
          },
          {
            "name": "limit",
            "required": False,
            "type": "number($int)",
            "description": "限制最多回傳的資料，預設為回傳全部筆數"
          },
          {
            "name": "offset",
            "required": False,
            "type": "number($int)",
            "description": "指定從第幾筆後開始回傳，預設為第 0 筆開始回傳"
          },
          {
            "name": "format",
            "required": False,
            "type": "string",
            "description": "回傳資料格式，預設為 json 格式Available values: JSON, XML--JSONXML"
          },
          {
            "name": "locationName",
            "required": False,
            "type": "array[string]",
            "description": "各縣市所對應鄉鎮名稱，請參考https://opendata.cwa.gov.tw/opendatadoc/Opendata_City.pdf，附錄 A『全臺縣市鄉鎮對照表』，預設為全部回傳"
          },
          {
            "name": "elementName",
            "required": False,
            "type": "array[string]",
            "description": "天氣預報因子，預設為全部回傳Available values: Wx, PoP12h, AT, T, RH, CI, WeatherDescription, PoP6h, WS, WD, Td--WxPoP12hATTRHCIWeatherDescriptionPoP6hWSWDTd"
          },
          {
            "name": "sort",
            "required": False,
            "type": "string",
            "description": "同時對 「startTime」，「endTime」，「dataTime」 做升冪排序，預設不排序Available values: time--time"
          },
          {
            "name": "startTime",
            "required": False,
            "type": "array[string]",
            "description": "時間因子，格式為「yyyy-MM-ddThh:mm:ss」，預設為全部回傳"
          },
          {
            "name": "dataTime",
            "required": False,
            "type": "array[string]",
            "description": "時間因子，格式為「yyyy-MM-ddThh:mm:ss」，預設為全部回傳"
          },
          {
            "name": "timeFrom",
            "required": False,
            "type": "string($date-time)",
            "description": "時間區段:時間從「timeFrom」 開始篩選，直到內容之最後時間，並可與參數 「timeTo 合併使用，格式為「yyyy-MM-ddThh:mm:ss」， 若使用參數「startTime」或「dataTime」，則參數「timeFrom」的篩選資料則會失效，預設為全部回傳"
          },
          {
            "name": "timeTo",
            "required": False,
            "type": "string($date-time)",
            "description": "時間區段，篩選需要之時間區段，時間從內容之最初時間開始篩選，直到 「timeTo」，並可與參數 「timeFrom」 合併使用，格式為「yyyy-MM-ddThh:mm:ss」，使用「startTime」或「dataTime」，則參數「timeTo」的篩選資料則會失效，預設為全部回傳"
          }
        ]
      },
      {
        "path": "/v1/rest/datastore/F-D0047-019",
        "dataId": "F-D0047-019",
        "summary": "鄉鎮天氣預報-彰化縣未來1週天氣預報",
        "description": "臺灣各鄉鎮市區預報資料-臺灣各鄉鎮市區未來2天(逐3小時)及未來1週天氣預報",
        "parameters": [
          {
            "name": "Authorization",
            "required": True,
            "type": "string",
            "description": "氣象開放資料平台會員授權碼"
          },
          {
            "name": "limit",
            "required": False,
            "type": "number($int)",
            "description": "限制最多回傳的資料，預設為回傳全部筆數"
          },
          {
            "name": "offset",
            "required": False,
            "type": "number($int)",
            "description": "指定從第幾筆後開始回傳，預設為第 0 筆開始回傳"
          },
          {
            "name": "format",
            "required": False,
            "type": "string",
            "description": "回傳資料格式，預設為 json 格式Available values: JSON, XML--JSONXML"
          },
          {
            "name": "locationName",
            "required": False,
            "type": "array[string]",
            "description": "各縣市所對應鄉鎮名稱，請參考https://opendata.cwa.gov.tw/opendatadoc/Opendata_City.pdf，附錄 A『全臺縣市鄉鎮對照表』，預設為全部回傳"
          },
          {
            "name": "elementName",
            "required": False,
            "type": "array[string]",
            "description": "天氣預報因子，預設為全部回傳Available values: MinCI, MaxAT, MaxCI, MinT, UVI, MinAT, MaxT, WS, WD, Td, PoP12h, T, RH, Wx, WeatherDescription--MinCIMaxATMaxCIMinTUVIMinATMaxTWSWDTdPoP12hTRHWxWeatherDescription"
          },
          {
            "name": "sort",
            "required": False,
            "type": "string",
            "description": "同時對 「startTime」，「endTime」，「dataTime」 做升冪排序，預設不排序Available values: time--time"
          },
          {
            "name": "startTime",
            "required": False,
            "type": "array[string]",
            "description": "時間因子，格式為「yyyy-MM-ddThh:mm:ss」，預設為全部回傳"
          },
          {
            "name": "dataTime",
            "required": False,
            "type": "array[string]",
            "description": "時間因子，格式為「yyyy-MM-ddThh:mm:ss」，預設為全部回傳"
          },
          {
            "name": "timeFrom",
            "required": False,
            "type": "string($date-time)",
            "description": "時間區段:時間從「timeFrom」 開始篩選，直到內容之最後時間，並可與參數 「timeTo 合併使用，格式為「yyyy-MM-ddThh:mm:ss」， 若使用參數「startTime」或「dataTime」，則參數「timeFrom」的篩選資料則會失效，預設為全部回傳"
          },
          {
            "name": "timeTo",
            "required": False,
            "type": "string($date-time)",
            "description": "時間區段，篩選需要之時間區段，時間從內容之最初時間開始篩選，直到 「timeTo」，並可與參數 「timeFrom」 合併使用，格式為「yyyy-MM-ddThh:mm:ss」，使用「startTime」或「dataTime」，則參數「timeTo」的篩選資料則會失效，預設為全部回傳"
          }
        ]
      },
      {
        "path": "/v1/rest/datastore/F-D0047-021",
        "dataId": "F-D0047-021",
        "summary": "鄉鎮天氣預報-南投縣未來2天天氣預報",
        "description": "臺灣各鄉鎮市區預報資料-臺灣各鄉鎮市區未來2天(逐3小時)及未來1週天氣預報",
        "parameters": [
          {
            "name": "Authorization",
            "required": True,
            "type": "string",
            "description": "氣象開放資料平台會員授權碼"
          },
          {
            "name": "limit",
            "required": False,
            "type": "number($int)",
            "description": "限制最多回傳的資料，預設為回傳全部筆數"
          },
          {
            "name": "offset",
            "required": False,
            "type": "number($int)",
            "description": "指定從第幾筆後開始回傳，預設為第 0 筆開始回傳"
          },
          {
            "name": "format",
            "required": False,
            "type": "string",
            "description": "回傳資料格式，預設為 json 格式Available values: JSON, XML--JSONXML"
          },
          {
            "name": "locationName",
            "required": False,
            "type": "array[string]",
            "description": "各縣市所對應鄉鎮名稱，請參考https://opendata.cwa.gov.tw/opendatadoc/Opendata_City.pdf，附錄 A『全臺縣市鄉鎮對照表』，預設為全部回傳"
          },
          {
            "name": "elementName",
            "required": False,
            "type": "array[string]",
            "description": "天氣預報因子，預設為全部回傳Available values: Wx, PoP12h, AT, T, RH, CI, WeatherDescription, PoP6h, WS, WD, Td--WxPoP12hATTRHCIWeatherDescriptionPoP6hWSWDTd"
          },
          {
            "name": "sort",
            "required": False,
            "type": "string",
            "description": "同時對 「startTime」，「endTime」，「dataTime」 做升冪排序，預設不排序Available values: time--time"
          },
          {
            "name": "startTime",
            "required": False,
            "type": "array[string]",
            "description": "時間因子，格式為「yyyy-MM-ddThh:mm:ss」，預設為全部回傳"
          },
          {
            "name": "dataTime",
            "required": False,
            "type": "array[string]",
            "description": "時間因子，格式為「yyyy-MM-ddThh:mm:ss」，預設為全部回傳"
          },
          {
            "name": "timeFrom",
            "required": False,
            "type": "string($date-time)",
            "description": "時間區段:時間從「timeFrom」 開始篩選，直到內容之最後時間，並可與參數 「timeTo 合併使用，格式為「yyyy-MM-ddThh:mm:ss」， 若使用參數「startTime」或「dataTime」，則參數「timeFrom」的篩選資料則會失效，預設為全部回傳"
          },
          {
            "name": "timeTo",
            "required": False,
            "type": "string($date-time)",
            "description": "時間區段，篩選需要之時間區段，時間從內容之最初時間開始篩選，直到 「timeTo」，並可與參數 「timeFrom」 合併使用，格式為「yyyy-MM-ddThh:mm:ss」，使用「startTime」或「dataTime」，則參數「timeTo」的篩選資料則會失效，預設為全部回傳"
          }
        ]
      },
      {
        "path": "/v1/rest/datastore/F-D0047-023",
        "dataId": "F-D0047-023",
        "summary": "鄉鎮天氣預報-南投縣未來1週天氣預報",
        "description": "臺灣各鄉鎮市區預報資料-臺灣各鄉鎮市區未來2天(逐3小時)及未來1週天氣預報",
        "parameters": [
          {
            "name": "Authorization",
            "required": True,
            "type": "string",
            "description": "氣象開放資料平台會員授權碼"
          },
          {
            "name": "limit",
            "required": False,
            "type": "number($int)",
            "description": "限制最多回傳的資料，預設為回傳全部筆數"
          },
          {
            "name": "offset",
            "required": False,
            "type": "number($int)",
            "description": "指定從第幾筆後開始回傳，預設為第 0 筆開始回傳"
          },
          {
            "name": "format",
            "required": False,
            "type": "string",
            "description": "回傳資料格式，預設為 json 格式Available values: JSON, XML--JSONXML"
          },
          {
            "name": "locationName",
            "required": False,
            "type": "array[string]",
            "description": "各縣市所對應鄉鎮名稱，請參考https://opendata.cwa.gov.tw/opendatadoc/Opendata_City.pdf，附錄 A『全臺縣市鄉鎮對照表』，預設為全部回傳"
          },
          {
            "name": "elementName",
            "required": False,
            "type": "array[string]",
            "description": "天氣預報因子，預設為全部回傳Available values: MinCI, MaxAT, MaxCI, MinT, UVI, MinAT, MaxT, WS, WD, Td, PoP12h, T, RH, Wx, WeatherDescription--MinCIMaxATMaxCIMinTUVIMinATMaxTWSWDTdPoP12hTRHWxWeatherDescription"
          },
          {
            "name": "sort",
            "required": False,
            "type": "string",
            "description": "同時對 「startTime」，「endTime」，「dataTime」 做升冪排序，預設不排序Available values: time--time"
          },
          {
            "name": "startTime",
            "required": False,
            "type": "array[string]",
            "description": "時間因子，格式為「yyyy-MM-ddThh:mm:ss」，預設為全部回傳"
          },
          {
            "name": "dataTime",
            "required": False,
            "type": "array[string]",
            "description": "時間因子，格式為「yyyy-MM-ddThh:mm:ss」，預設為全部回傳"
          },
          {
            "name": "timeFrom",
            "required": False,
            "type": "string($date-time)",
            "description": "時間區段:時間從「timeFrom」 開始篩選，直到內容之最後時間，並可與參數 「timeTo 合併使用，格式為「yyyy-MM-ddThh:mm:ss」， 若使用參數「startTime」或「dataTime」，則參數「timeFrom」的篩選資料則會失效，預設為全部回傳"
          },
          {
            "name": "timeTo",
            "required": False,
            "type": "string($date-time)",
            "description": "時間區段，篩選需要之時間區段，時間從內容之最初時間開始篩選，直到 「timeTo」，並可與參數 「timeFrom」 合併使用，格式為「yyyy-MM-ddThh:mm:ss」，使用「startTime」或「dataTime」，則參數「timeTo」的篩選資料則會失效，預設為全部回傳"
          }
        ]
      },
      {
        "path": "/v1/rest/datastore/F-D0047-025",
        "dataId": "F-D0047-025",
        "summary": "鄉鎮天氣預報-雲林縣未來2天天氣預報",
        "description": "臺灣各鄉鎮市區預報資料-臺灣各鄉鎮市區未來2天(逐3小時)及未來1週天氣預報",
        "parameters": [
          {
            "name": "Authorization",
            "required": True,
            "type": "string",
            "description": "氣象開放資料平台會員授權碼"
          },
          {
            "name": "limit",
            "required": False,
            "type": "number($int)",
            "description": "限制最多回傳的資料，預設為回傳全部筆數"
          },
          {
            "name": "offset",
            "required": False,
            "type": "number($int)",
            "description": "指定從第幾筆後開始回傳，預設為第 0 筆開始回傳"
          },
          {
            "name": "format",
            "required": False,
            "type": "string",
            "description": "回傳資料格式，預設為 json 格式Available values: JSON, XML--JSONXML"
          },
          {
            "name": "locationName",
            "required": False,
            "type": "array[string]",
            "description": "各縣市所對應鄉鎮名稱，請參考https://opendata.cwa.gov.tw/opendatadoc/Opendata_City.pdf，附錄 A『全臺縣市鄉鎮對照表』，預設為全部回傳"
          },
          {
            "name": "elementName",
            "required": False,
            "type": "array[string]",
            "description": "天氣預報因子，預設為全部回傳Available values: Wx, PoP12h, AT, T, RH, CI, WeatherDescription, PoP6h, WS, WD, Td--WxPoP12hATTRHCIWeatherDescriptionPoP6hWSWDTd"
          },
          {
            "name": "sort",
            "required": False,
            "type": "string",
            "description": "同時對 「startTime」，「endTime」，「dataTime」 做升冪排序，預設不排序Available values: time--time"
          },
          {
            "name": "startTime",
            "required": False,
            "type": "array[string]",
            "description": "時間因子，格式為「yyyy-MM-ddThh:mm:ss」，預設為全部回傳"
          },
          {
            "name": "dataTime",
            "required": False,
            "type": "array[string]",
            "description": "時間因子，格式為「yyyy-MM-ddThh:mm:ss」，預設為全部回傳"
          },
          {
            "name": "timeFrom",
            "required": False,
            "type": "string($date-time)",
            "description": "時間區段:時間從「timeFrom」 開始篩選，直到內容之最後時間，並可與參數 「timeTo 合併使用，格式為「yyyy-MM-ddThh:mm:ss」， 若使用參數「startTime」或「dataTime」，則參數「timeFrom」的篩選資料則會失效，預設為全部回傳"
          },
          {
            "name": "timeTo",
            "required": False,
            "type": "string($date-time)",
            "description": "時間區段，篩選需要之時間區段，時間從內容之最初時間開始篩選，直到 「timeTo」，並可與參數 「timeFrom」 合併使用，格式為「yyyy-MM-ddThh:mm:ss」，使用「startTime」或「dataTime」，則參數「timeTo」的篩選資料則會失效，預設為全部回傳"
          }
        ]
      },
      {
        "path": "/v1/rest/datastore/F-D0047-027",
        "dataId": "F-D0047-027",
        "summary": "鄉鎮天氣預報-雲林縣未來1週天氣預報",
        "description": "臺灣各鄉鎮市區預報資料-臺灣各鄉鎮市區未來2天(逐3小時)及未來1週天氣預報",
        "parameters": [
          {
            "name": "Authorization",
            "required": True,
            "type": "string",
            "description": "氣象開放資料平台會員授權碼"
          },
          {
            "name": "limit",
            "required": False,
            "type": "number($int)",
            "description": "限制最多回傳的資料，預設為回傳全部筆數"
          },
          {
            "name": "offset",
            "required": False,
            "type": "number($int)",
            "description": "指定從第幾筆後開始回傳，預設為第 0 筆開始回傳"
          },
          {
            "name": "format",
            "required": False,
            "type": "string",
            "description": "回傳資料格式，預設為 json 格式Available values: JSON, XML--JSONXML"
          },
          {
            "name": "locationName",
            "required": False,
            "type": "array[string]",
            "description": "各縣市所對應鄉鎮名稱，請參考https://opendata.cwa.gov.tw/opendatadoc/Opendata_City.pdf，附錄 A『全臺縣市鄉鎮對照表』，預設為全部回傳"
          },
          {
            "name": "elementName",
            "required": False,
            "type": "array[string]",
            "description": "天氣預報因子，預設為全部回傳Available values: MinCI, MaxAT, MaxCI, MinT, UVI, MinAT, MaxT, WS, WD, Td, PoP12h, T, RH, Wx, WeatherDescription--MinCIMaxATMaxCIMinTUVIMinATMaxTWSWDTdPoP12hTRHWxWeatherDescription"
          },
          {
            "name": "sort",
            "required": False,
            "type": "string",
            "description": "同時對 「startTime」，「endTime」，「dataTime」 做升冪排序，預設不排序Available values: time--time"
          },
          {
            "name": "startTime",
            "required": False,
            "type": "array[string]",
            "description": "時間因子，格式為「yyyy-MM-ddThh:mm:ss」，預設為全部回傳"
          },
          {
            "name": "dataTime",
            "required": False,
            "type": "array[string]",
            "description": "時間因子，格式為「yyyy-MM-ddThh:mm:ss」，預設為全部回傳"
          },
          {
            "name": "timeFrom",
            "required": False,
            "type": "string($date-time)",
            "description": "時間區段:時間從「timeFrom」 開始篩選，直到內容之最後時間，並可與參數 「timeTo 合併使用，格式為「yyyy-MM-ddThh:mm:ss」， 若使用參數「startTime」或「dataTime」，則參數「timeFrom」的篩選資料則會失效，預設為全部回傳"
          },
          {
            "name": "timeTo",
            "required": False,
            "type": "string($date-time)",
            "description": "時間區段，篩選需要之時間區段，時間從內容之最初時間開始篩選，直到 「timeTo」，並可與參數 「timeFrom」 合併使用，格式為「yyyy-MM-ddThh:mm:ss」，使用「startTime」或「dataTime」，則參數「timeTo」的篩選資料則會失效，預設為全部回傳"
          }
        ]
      },
      {
        "path": "/v1/rest/datastore/F-D0047-029",
        "dataId": "F-D0047-029",
        "summary": "鄉鎮天氣預報-嘉義縣未來2天天氣預報",
        "description": "臺灣各鄉鎮市區預報資料-臺灣各鄉鎮市區未來2天(逐3小時)及未來1週天氣預報",
        "parameters": [
          {
            "name": "Authorization",
            "required": True,
            "type": "string",
            "description": "氣象開放資料平台會員授權碼"
          },
          {
            "name": "limit",
            "required": False,
            "type": "number($int)",
            "description": "限制最多回傳的資料，預設為回傳全部筆數"
          },
          {
            "name": "offset",
            "required": False,
            "type": "number($int)",
            "description": "指定從第幾筆後開始回傳，預設為第 0 筆開始回傳"
          },
          {
            "name": "format",
            "required": False,
            "type": "string",
            "description": "回傳資料格式，預設為 json 格式Available values: JSON, XML--JSONXML"
          },
          {
            "name": "locationName",
            "required": False,
            "type": "array[string]",
            "description": "各縣市所對應鄉鎮名稱，請參考https://opendata.cwa.gov.tw/opendatadoc/Opendata_City.pdf，附錄 A『全臺縣市鄉鎮對照表』，預設為全部回傳"
          },
          {
            "name": "elementName",
            "required": False,
            "type": "array[string]",
            "description": "天氣預報因子，預設為全部回傳Available values: Wx, PoP12h, AT, T, RH, CI, WeatherDescription, PoP6h, WS, WD, Td--WxPoP12hATTRHCIWeatherDescriptionPoP6hWSWDTd"
          },
          {
            "name": "sort",
            "required": False,
            "type": "string",
            "description": "同時對 「startTime」，「endTime」，「dataTime」 做升冪排序，預設不排序Available values: time--time"
          },
          {
            "name": "startTime",
            "required": False,
            "type": "array[string]",
            "description": "時間因子，格式為「yyyy-MM-ddThh:mm:ss」，預設為全部回傳"
          },
          {
            "name": "dataTime",
            "required": False,
            "type": "array[string]",
            "description": "時間因子，格式為「yyyy-MM-ddThh:mm:ss」，預設為全部回傳"
          },
          {
            "name": "timeFrom",
            "required": False,
            "type": "string($date-time)",
            "description": "時間區段:時間從「timeFrom」 開始篩選，直到內容之最後時間，並可與參數 「timeTo 合併使用，格式為「yyyy-MM-ddThh:mm:ss」， 若使用參數「startTime」或「dataTime」，則參數「timeFrom」的篩選資料則會失效，預設為全部回傳"
          },
          {
            "name": "timeTo",
            "required": False,
            "type": "string($date-time)",
            "description": "時間區段，篩選需要之時間區段，時間從內容之最初時間開始篩選，直到 「timeTo」，並可與參數 「timeFrom」 合併使用，格式為「yyyy-MM-ddThh:mm:ss」，使用「startTime」或「dataTime」，則參數「timeTo」的篩選資料則會失效，預設為全部回傳"
          }
        ]
      },
      {
        "path": "/v1/rest/datastore/F-D0047-031",
        "dataId": "F-D0047-031",
        "summary": "鄉鎮天氣預報-嘉義縣未來1週天氣預報",
        "description": "臺灣各鄉鎮市區預報資料-臺灣各鄉鎮市區未來2天(逐3小時)及未來1週天氣預報",
        "parameters": [
          {
            "name": "Authorization",
            "required": True,
            "type": "string",
            "description": "氣象開放資料平台會員授權碼"
          },
          {
            "name": "limit",
            "required": False,
            "type": "number($int)",
            "description": "限制最多回傳的資料，預設為回傳全部筆數"
          },
          {
            "name": "offset",
            "required": False,
            "type": "number($int)",
            "description": "指定從第幾筆後開始回傳，預設為第 0 筆開始回傳"
          },
          {
            "name": "format",
            "required": False,
            "type": "string",
            "description": "回傳資料格式，預設為 json 格式Available values: JSON, XML--JSONXML"
          },
          {
            "name": "locationName",
            "required": False,
            "type": "array[string]",
            "description": "各縣市所對應鄉鎮名稱，請參考https://opendata.cwa.gov.tw/opendatadoc/Opendata_City.pdf，附錄 A『全臺縣市鄉鎮對照表』，預設為全部回傳"
          },
          {
            "name": "elementName",
            "required": False,
            "type": "array[string]",
            "description": "天氣預報因子，預設為全部回傳Available values: MinCI, MaxAT, MaxCI, MinT, UVI, MinAT, MaxT, WS, WD, Td, PoP12h, T, RH, Wx, WeatherDescription--MinCIMaxATMaxCIMinTUVIMinATMaxTWSWDTdPoP12hTRHWxWeatherDescription"
          },
          {
            "name": "sort",
            "required": False,
            "type": "string",
            "description": "同時對 「startTime」，「endTime」，「dataTime」 做升冪排序，預設不排序Available values: time--time"
          },
          {
            "name": "startTime",
            "required": False,
            "type": "array[string]",
            "description": "時間因子，格式為「yyyy-MM-ddThh:mm:ss」，預設為全部回傳"
          },
          {
            "name": "dataTime",
            "required": False,
            "type": "array[string]",
            "description": "時間因子，格式為「yyyy-MM-ddThh:mm:ss」，預設為全部回傳"
          },
          {
            "name": "timeFrom",
            "required": False,
            "type": "string($date-time)",
            "description": "時間區段:時間從「timeFrom」 開始篩選，直到內容之最後時間，並可與參數 「timeTo 合併使用，格式為「yyyy-MM-ddThh:mm:ss」， 若使用參數「startTime」或「dataTime」，則參數「timeFrom」的篩選資料則會失效，預設為全部回傳"
          },
          {
            "name": "timeTo",
            "required": False,
            "type": "string($date-time)",
            "description": "時間區段，篩選需要之時間區段，時間從內容之最初時間開始篩選，直到 「timeTo」，並可與參數 「timeFrom」 合併使用，格式為「yyyy-MM-ddThh:mm:ss」，使用「startTime」或「dataTime」，則參數「timeTo」的篩選資料則會失效，預設為全部回傳"
          }
        ]
      },
      {
        "path": "/v1/rest/datastore/F-D0047-033",
        "dataId": "F-D0047-033",
        "summary": "鄉鎮天氣預報-屏東縣未來2天天氣預報",
        "description": "臺灣各鄉鎮市區預報資料-臺灣各鄉鎮市區未來2天(逐3小時)及未來1週天氣預報",
        "parameters": [
          {
            "name": "Authorization",
            "required": True,
            "type": "string",
            "description": "氣象開放資料平台會員授權碼"
          },
          {
            "name": "limit",
            "required": False,
            "type": "number($int)",
            "description": "限制最多回傳的資料，預設為回傳全部筆數"
          },
          {
            "name": "offset",
            "required": False,
            "type": "number($int)",
            "description": "指定從第幾筆後開始回傳，預設為第 0 筆開始回傳"
          },
          {
            "name": "format",
            "required": False,
            "type": "string",
            "description": "回傳資料格式，預設為 json 格式Available values: JSON, XML--JSONXML"
          },
          {
            "name": "locationName",
            "required": False,
            "type": "array[string]",
            "description": "各縣市所對應鄉鎮名稱，請參考https://opendata.cwa.gov.tw/opendatadoc/Opendata_City.pdf，附錄 A『全臺縣市鄉鎮對照表』，預設為全部回傳"
          },
          {
            "name": "elementName",
            "required": False,
            "type": "array[string]",
            "description": "天氣預報因子，預設為全部回傳Available values: Wx, PoP12h, AT, T, RH, CI, WeatherDescription, PoP6h, WS, WD, Td--WxPoP12hATTRHCIWeatherDescriptionPoP6hWSWDTd"
          },
          {
            "name": "sort",
            "required": False,
            "type": "string",
            "description": "同時對 「startTime」，「endTime」，「dataTime」 做升冪排序，預設不排序Available values: time--time"
          },
          {
            "name": "startTime",
            "required": False,
            "type": "array[string]",
            "description": "時間因子，格式為「yyyy-MM-ddThh:mm:ss」，預設為全部回傳"
          },
          {
            "name": "dataTime",
            "required": False,
            "type": "array[string]",
            "description": "時間因子，格式為「yyyy-MM-ddThh:mm:ss」，預設為全部回傳"
          },
          {
            "name": "timeFrom",
            "required": False,
            "type": "string($date-time)",
            "description": "時間區段:時間從「timeFrom」 開始篩選，直到內容之最後時間，並可與參數 「timeTo 合併使用，格式為「yyyy-MM-ddThh:mm:ss」， 若使用參數「startTime」或「dataTime」，則參數「timeFrom」的篩選資料則會失效，預設為全部回傳"
          },
          {
            "name": "timeTo",
            "required": False,
            "type": "string($date-time)",
            "description": "時間區段，篩選需要之時間區段，時間從內容之最初時間開始篩選，直到 「timeTo」，並可與參數 「timeFrom」 合併使用，格式為「yyyy-MM-ddThh:mm:ss」，使用「startTime」或「dataTime」，則參數「timeTo」的篩選資料則會失效，預設為全部回傳"
          }
        ]
      },
      {
        "path": "/v1/rest/datastore/F-D0047-035",
        "dataId": "F-D0047-035",
        "summary": "鄉鎮天氣預報-屏東縣未來1週天氣預報",
        "description": "臺灣各鄉鎮市區預報資料-臺灣各鄉鎮市區未來2天(逐3小時)及未來1週天氣預報",
        "parameters": [
          {
            "name": "Authorization",
            "required": True,
            "type": "string",
            "description": "氣象開放資料平台會員授權碼"
          },
          {
            "name": "limit",
            "required": False,
            "type": "number($int)",
            "description": "限制最多回傳的資料，預設為回傳全部筆數"
          },
          {
            "name": "offset",
            "required": False,
            "type": "number($int)",
            "description": "指定從第幾筆後開始回傳，預設為第 0 筆開始回傳"
          },
          {
            "name": "format",
            "required": False,
            "type": "string",
            "description": "回傳資料格式，預設為 json 格式Available values: JSON, XML--JSONXML"
          },
          {
            "name": "locationName",
            "required": False,
            "type": "array[string]",
            "description": "各縣市所對應鄉鎮名稱，請參考https://opendata.cwa.gov.tw/opendatadoc/Opendata_City.pdf，附錄 A『全臺縣市鄉鎮對照表』，預設為全部回傳"
          },
          {
            "name": "elementName",
            "required": False,
            "type": "array[string]",
            "description": "天氣預報因子，預設為全部回傳Available values: MinCI, MaxAT, MaxCI, MinT, UVI, MinAT, MaxT, WS, WD, Td, PoP12h, T, RH, Wx, WeatherDescription--MinCIMaxATMaxCIMinTUVIMinATMaxTWSWDTdPoP12hTRHWxWeatherDescription"
          },
          {
            "name": "sort",
            "required": False,
            "type": "string",
            "description": "同時對 「startTime」，「endTime」，「dataTime」 做升冪排序，預設不排序Available values: time--time"
          },
          {
            "name": "startTime",
            "required": False,
            "type": "array[string]",
            "description": "時間因子，格式為「yyyy-MM-ddThh:mm:ss」，預設為全部回傳"
          },
          {
            "name": "dataTime",
            "required": False,
            "type": "array[string]",
            "description": "時間因子，格式為「yyyy-MM-ddThh:mm:ss」，預設為全部回傳"
          },
          {
            "name": "timeFrom",
            "required": False,
            "type": "string($date-time)",
            "description": "時間區段:時間從「timeFrom」 開始篩選，直到內容之最後時間，並可與參數 「timeTo 合併使用，格式為「yyyy-MM-ddThh:mm:ss」， 若使用參數「startTime」或「dataTime」，則參數「timeFrom」的篩選資料則會失效，預設為全部回傳"
          },
          {
            "name": "timeTo",
            "required": False,
            "type": "string($date-time)",
            "description": "時間區段，篩選需要之時間區段，時間從內容之最初時間開始篩選，直到 「timeTo」，並可與參數 「timeFrom」 合併使用，格式為「yyyy-MM-ddThh:mm:ss」，使用「startTime」或「dataTime」，則參數「timeTo」的篩選資料則會失效，預設為全部回傳"
          }
        ]
      },
      {
        "path": "/v1/rest/datastore/F-D0047-037",
        "dataId": "F-D0047-037",
        "summary": "鄉鎮天氣預報-臺東縣未來2天天氣預報",
        "description": "臺灣各鄉鎮市區預報資料-臺灣各鄉鎮市區未來2天(逐3小時)及未來1週天氣預報",
        "parameters": [
          {
            "name": "Authorization",
            "required": True,
            "type": "string",
            "description": "氣象開放資料平台會員授權碼"
          },
          {
            "name": "limit",
            "required": False,
            "type": "number($int)",
            "description": "限制最多回傳的資料，預設為回傳全部筆數"
          },
          {
            "name": "offset",
            "required": False,
            "type": "number($int)",
            "description": "指定從第幾筆後開始回傳，預設為第 0 筆開始回傳"
          },
          {
            "name": "format",
            "required": False,
            "type": "string",
            "description": "回傳資料格式，預設為 json 格式Available values: JSON, XML--JSONXML"
          },
          {
            "name": "locationName",
            "required": False,
            "type": "array[string]",
            "description": "各縣市所對應鄉鎮名稱，請參考https://opendata.cwa.gov.tw/opendatadoc/Opendata_City.pdf，附錄 A『全臺縣市鄉鎮對照表』，預設為全部回傳"
          },
          {
            "name": "elementName",
            "required": False,
            "type": "array[string]",
            "description": "天氣預報因子，預設為全部回傳Available values: Wx, PoP12h, AT, T, RH, CI, WeatherDescription, PoP6h, WS, WD, Td--WxPoP12hATTRHCIWeatherDescriptionPoP6hWSWDTd"
          },
          {
            "name": "sort",
            "required": False,
            "type": "string",
            "description": "同時對 「startTime」，「endTime」，「dataTime」 做升冪排序，預設不排序Available values: time--time"
          },
          {
            "name": "startTime",
            "required": False,
            "type": "array[string]",
            "description": "時間因子，格式為「yyyy-MM-ddThh:mm:ss」，預設為全部回傳"
          },
          {
            "name": "dataTime",
            "required": False,
            "type": "array[string]",
            "description": "時間因子，格式為「yyyy-MM-ddThh:mm:ss」，預設為全部回傳"
          },
          {
            "name": "timeFrom",
            "required": False,
            "type": "string($date-time)",
            "description": "時間區段:時間從「timeFrom」 開始篩選，直到內容之最後時間，並可與參數 「timeTo 合併使用，格式為「yyyy-MM-ddThh:mm:ss」， 若使用參數「startTime」或「dataTime」，則參數「timeFrom」的篩選資料則會失效，預設為全部回傳"
          },
          {
            "name": "timeTo",
            "required": False,
            "type": "string($date-time)",
            "description": "時間區段，篩選需要之時間區段，時間從內容之最初時間開始篩選，直到 「timeTo」，並可與參數 「timeFrom」 合併使用，格式為「yyyy-MM-ddThh:mm:ss」，使用「startTime」或「dataTime」，則參數「timeTo」的篩選資料則會失效，預設為全部回傳"
          }
        ]
      },
      {
        "path": "/v1/rest/datastore/F-D0047-039",
        "dataId": "F-D0047-039",
        "summary": "鄉鎮天氣預報-臺東縣未來1週天氣預報",
        "description": "臺灣各鄉鎮市區預報資料-臺灣各鄉鎮市區未來2天(逐3小時)及未來1週天氣預報",
        "parameters": [
          {
            "name": "Authorization",
            "required": True,
            "type": "string",
            "description": "氣象開放資料平台會員授權碼"
          },
          {
            "name": "limit",
            "required": False,
            "type": "number($int)",
            "description": "限制最多回傳的資料，預設為回傳全部筆數"
          },
          {
            "name": "offset",
            "required": False,
            "type": "number($int)",
            "description": "指定從第幾筆後開始回傳，預設為第 0 筆開始回傳"
          },
          {
            "name": "format",
            "required": False,
            "type": "string",
            "description": "回傳資料格式，預設為 json 格式Available values: JSON, XML--JSONXML"
          },
          {
            "name": "locationName",
            "required": False,
            "type": "array[string]",
            "description": "各縣市所對應鄉鎮名稱，請參考https://opendata.cwa.gov.tw/opendatadoc/Opendata_City.pdf，附錄 A『全臺縣市鄉鎮對照表』，預設為全部回傳"
          },
          {
            "name": "elementName",
            "required": False,
            "type": "array[string]",
            "description": "天氣預報因子，預設為全部回傳Available values: MinCI, MaxAT, MaxCI, MinT, UVI, MinAT, MaxT, WS, WD, Td, PoP12h, T, RH, Wx, WeatherDescription--MinCIMaxATMaxCIMinTUVIMinATMaxTWSWDTdPoP12hTRHWxWeatherDescription"
          },
          {
            "name": "sort",
            "required": False,
            "type": "string",
            "description": "同時對 「startTime」，「endTime」，「dataTime」 做升冪排序，預設不排序Available values: time--time"
          },
          {
            "name": "startTime",
            "required": False,
            "type": "array[string]",
            "description": "時間因子，格式為「yyyy-MM-ddThh:mm:ss」，預設為全部回傳"
          },
          {
            "name": "dataTime",
            "required": False,
            "type": "array[string]",
            "description": "時間因子，格式為「yyyy-MM-ddThh:mm:ss」，預設為全部回傳"
          },
          {
            "name": "timeFrom",
            "required": False,
            "type": "string($date-time)",
            "description": "時間區段:時間從「timeFrom」 開始篩選，直到內容之最後時間，並可與參數 「timeTo 合併使用，格式為「yyyy-MM-ddThh:mm:ss」， 若使用參數「startTime」或「dataTime」，則參數「timeFrom」的篩選資料則會失效，預設為全部回傳"
          },
          {
            "name": "timeTo",
            "required": False,
            "type": "string($date-time)",
            "description": "時間區段，篩選需要之時間區段，時間從內容之最初時間開始篩選，直到 「timeTo」，並可與參數 「timeFrom」 合併使用，格式為「yyyy-MM-ddThh:mm:ss」，使用「startTime」或「dataTime」，則參數「timeTo」的篩選資料則會失效，預設為全部回傳"
          }
        ]
      },
      {
        "path": "/v1/rest/datastore/F-D0047-041",
        "dataId": "F-D0047-041",
        "summary": "鄉鎮天氣預報-花蓮縣未來2天天氣預報",
        "description": "臺灣各鄉鎮市區預報資料-臺灣各鄉鎮市區未來2天(逐3小時)及未來1週天氣預報",
        "parameters": [
          {
            "name": "Authorization",
            "required": True,
            "type": "string",
            "description": "氣象開放資料平台會員授權碼"
          },
          {
            "name": "limit",
            "required": False,
            "type": "number($int)",
            "description": "限制最多回傳的資料，預設為回傳全部筆數"
          },
          {
            "name": "offset",
            "required": False,
            "type": "number($int)",
            "description": "指定從第幾筆後開始回傳，預設為第 0 筆開始回傳"
          },
          {
            "name": "format",
            "required": False,
            "type": "string",
            "description": "回傳資料格式，預設為 json 格式Available values: JSON, XML--JSONXML"
          },
          {
            "name": "locationName",
            "required": False,
            "type": "array[string]",
            "description": "各縣市所對應鄉鎮名稱，請參考https://opendata.cwa.gov.tw/opendatadoc/Opendata_City.pdf，附錄 A『全臺縣市鄉鎮對照表』，預設為全部回傳"
          },
          {
            "name": "elementName",
            "required": False,
            "type": "array[string]",
            "description": "天氣預報因子，預設為全部回傳Available values: Wx, PoP12h, AT, T, RH, CI, WeatherDescription, PoP6h, WS, WD, Td--WxPoP12hATTRHCIWeatherDescriptionPoP6hWSWDTd"
          },
          {
            "name": "sort",
            "required": False,
            "type": "string",
            "description": "同時對 「startTime」，「endTime」，「dataTime」 做升冪排序，預設不排序Available values: time--time"
          },
          {
            "name": "startTime",
            "required": False,
            "type": "array[string]",
            "description": "時間因子，格式為「yyyy-MM-ddThh:mm:ss」，預設為全部回傳"
          },
          {
            "name": "dataTime",
            "required": False,
            "type": "array[string]",
            "description": "時間因子，格式為「yyyy-MM-ddThh:mm:ss」，預設為全部回傳"
          },
          {
            "name": "timeFrom",
            "required": False,
            "type": "string($date-time)",
            "description": "時間區段:時間從「timeFrom」 開始篩選，直到內容之最後時間，並可與參數 「timeTo 合併使用，格式為「yyyy-MM-ddThh:mm:ss」， 若使用參數「startTime」或「dataTime」，則參數「timeFrom」的篩選資料則會失效，預設為全部回傳"
          },
          {
            "name": "timeTo",
            "required": False,
            "type": "string($date-time)",
            "description": "時間區段，篩選需要之時間區段，時間從內容之最初時間開始篩選，直到 「timeTo」，並可與參數 「timeFrom」 合併使用，格式為「yyyy-MM-ddThh:mm:ss」，使用「startTime」或「dataTime」，則參數「timeTo」的篩選資料則會失效，預設為全部回傳"
          }
        ]
      },
      {
        "path": "/v1/rest/datastore/F-D0047-043",
        "dataId": "F-D0047-043",
        "summary": "鄉鎮天氣預報-花蓮縣未來1週天氣預報",
        "description": "臺灣各鄉鎮市區預報資料-臺灣各鄉鎮市區未來2天(逐3小時)及未來1週天氣預報",
        "parameters": [
          {
            "name": "Authorization",
            "required": True,
            "type": "string",
            "description": "氣象開放資料平台會員授權碼"
          },
          {
            "name": "limit",
            "required": False,
            "type": "number($int)",
            "description": "限制最多回傳的資料，預設為回傳全部筆數"
          },
          {
            "name": "offset",
            "required": False,
            "type": "number($int)",
            "description": "指定從第幾筆後開始回傳，預設為第 0 筆開始回傳"
          },
          {
            "name": "format",
            "required": False,
            "type": "string",
            "description": "回傳資料格式，預設為 json 格式Available values: JSON, XML--JSONXML"
          },
          {
            "name": "locationName",
            "required": False,
            "type": "array[string]",
            "description": "各縣市所對應鄉鎮名稱，請參考https://opendata.cwa.gov.tw/opendatadoc/Opendata_City.pdf，附錄 A『全臺縣市鄉鎮對照表』，預設為全部回傳"
          },
          {
            "name": "elementName",
            "required": False,
            "type": "array[string]",
            "description": "天氣預報因子，預設為全部回傳Available values: MinCI, MaxAT, MaxCI, MinT, UVI, MinAT, MaxT, WS, WD, Td, PoP12h, T, RH, Wx, WeatherDescription--MinCIMaxATMaxCIMinTUVIMinATMaxTWSWDTdPoP12hTRHWxWeatherDescription"
          },
          {
            "name": "sort",
            "required": False,
            "type": "string",
            "description": "同時對 「startTime」，「endTime」，「dataTime」 做升冪排序，預設不排序Available values: time--time"
          },
          {
            "name": "startTime",
            "required": False,
            "type": "array[string]",
            "description": "時間因子，格式為「yyyy-MM-ddThh:mm:ss」，預設為全部回傳"
          },
          {
            "name": "dataTime",
            "required": False,
            "type": "array[string]",
            "description": "時間因子，格式為「yyyy-MM-ddThh:mm:ss」，預設為全部回傳"
          },
          {
            "name": "timeFrom",
            "required": False,
            "type": "string($date-time)",
            "description": "時間區段:時間從「timeFrom」 開始篩選，直到內容之最後時間，並可與參數 「timeTo 合併使用，格式為「yyyy-MM-ddThh:mm:ss」， 若使用參數「startTime」或「dataTime」，則參數「timeFrom」的篩選資料則會失效，預設為全部回傳"
          },
          {
            "name": "timeTo",
            "required": False,
            "type": "string($date-time)",
            "description": "時間區段，篩選需要之時間區段，時間從內容之最初時間開始篩選，直到 「timeTo」，並可與參數 「timeFrom」 合併使用，格式為「yyyy-MM-ddThh:mm:ss」，使用「startTime」或「dataTime」，則參數「timeTo」的篩選資料則會失效，預設為全部回傳"
          }
        ]
      },
      {
        "path": "/v1/rest/datastore/F-D0047-045",
        "dataId": "F-D0047-045",
        "summary": "鄉鎮天氣預報-澎湖縣未來2天天氣預報",
        "description": "臺灣各鄉鎮市區預報資料-臺灣各鄉鎮市區未來2天(逐3小時)及未來1週天氣預報",
        "parameters": [
          {
            "name": "Authorization",
            "required": True,
            "type": "string",
            "description": "氣象開放資料平台會員授權碼"
          },
          {
            "name": "limit",
            "required": False,
            "type": "number($int)",
            "description": "限制最多回傳的資料，預設為回傳全部筆數"
          },
          {
            "name": "offset",
            "required": False,
            "type": "number($int)",
            "description": "指定從第幾筆後開始回傳，預設為第 0 筆開始回傳"
          },
          {
            "name": "format",
            "required": False,
            "type": "string",
            "description": "回傳資料格式，預設為 json 格式Available values: JSON, XML--JSONXML"
          },
          {
            "name": "locationName",
            "required": False,
            "type": "array[string]",
            "description": "各縣市所對應鄉鎮名稱，請參考https://opendata.cwa.gov.tw/opendatadoc/Opendata_City.pdf，附錄 A『全臺縣市鄉鎮對照表』，預設為全部回傳"
          },
          {
            "name": "elementName",
            "required": False,
            "type": "array[string]",
            "description": "天氣預報因子，預設為全部回傳Available values: Wx, PoP12h, AT, T, RH, CI, WeatherDescription, PoP6h, WS, WD, Td--WxPoP12hATTRHCIWeatherDescriptionPoP6hWSWDTd"
          },
          {
            "name": "sort",
            "required": False,
            "type": "string",
            "description": "同時對 「startTime」，「endTime」，「dataTime」 做升冪排序，預設不排序Available values: time--time"
          },
          {
            "name": "startTime",
            "required": False,
            "type": "array[string]",
            "description": "時間因子，格式為「yyyy-MM-ddThh:mm:ss」，預設為全部回傳"
          },
          {
            "name": "dataTime",
            "required": False,
            "type": "array[string]",
            "description": "時間因子，格式為「yyyy-MM-ddThh:mm:ss」，預設為全部回傳"
          },
          {
            "name": "timeFrom",
            "required": False,
            "type": "string($date-time)",
            "description": "時間區段:時間從「timeFrom」 開始篩選，直到內容之最後時間，並可與參數 「timeTo 合併使用，格式為「yyyy-MM-ddThh:mm:ss」， 若使用參數「startTime」或「dataTime」，則參數「timeFrom」的篩選資料則會失效，預設為全部回傳"
          },
          {
            "name": "timeTo",
            "required": False,
            "type": "string($date-time)",
            "description": "時間區段，篩選需要之時間區段，時間從內容之最初時間開始篩選，直到 「timeTo」，並可與參數 「timeFrom」 合併使用，格式為「yyyy-MM-ddThh:mm:ss」，使用「startTime」或「dataTime」，則參數「timeTo」的篩選資料則會失效，預設為全部回傳"
          }
        ]
      },
      {
        "path": "/v1/rest/datastore/F-D0047-047",
        "dataId": "F-D0047-047",
        "summary": "鄉鎮天氣預報-澎湖縣未來1週天氣預報",
        "description": "臺灣各鄉鎮市區預報資料-臺灣各鄉鎮市區未來2天(逐3小時)及未來1週天氣預報",
        "parameters": [
          {
            "name": "Authorization",
            "required": True,
            "type": "string",
            "description": "氣象開放資料平台會員授權碼"
          },
          {
            "name": "limit",
            "required": False,
            "type": "number($int)",
            "description": "限制最多回傳的資料，預設為回傳全部筆數"
          },
          {
            "name": "offset",
            "required": False,
            "type": "number($int)",
            "description": "指定從第幾筆後開始回傳，預設為第 0 筆開始回傳"
          },
          {
            "name": "format",
            "required": False,
            "type": "string",
            "description": "回傳資料格式，預設為 json 格式Available values: JSON, XML--JSONXML"
          },
          {
            "name": "locationName",
            "required": False,
            "type": "array[string]",
            "description": "各縣市所對應鄉鎮名稱，請參考https://opendata.cwa.gov.tw/opendatadoc/Opendata_City.pdf，附錄 A『全臺縣市鄉鎮對照表』，預設為全部回傳"
          },
          {
            "name": "elementName",
            "required": False,
            "type": "array[string]",
            "description": "天氣預報因子，預設為全部回傳Available values: MinCI, MaxAT, MaxCI, MinT, UVI, MinAT, MaxT, WS, WD, Td, PoP12h, T, RH, Wx, WeatherDescription--MinCIMaxATMaxCIMinTUVIMinATMaxTWSWDTdPoP12hTRHWxWeatherDescription"
          },
          {
            "name": "sort",
            "required": False,
            "type": "string",
            "description": "同時對 「startTime」，「endTime」，「dataTime」 做升冪排序，預設不排序Available values: time--time"
          },
          {
            "name": "startTime",
            "required": False,
            "type": "array[string]",
            "description": "時間因子，格式為「yyyy-MM-ddThh:mm:ss」，預設為全部回傳"
          },
          {
            "name": "dataTime",
            "required": False,
            "type": "array[string]",
            "description": "時間因子，格式為「yyyy-MM-ddThh:mm:ss」，預設為全部回傳"
          },
          {
            "name": "timeFrom",
            "required": False,
            "type": "string($date-time)",
            "description": "時間區段:時間從「timeFrom」 開始篩選，直到內容之最後時間，並可與參數 「timeTo 合併使用，格式為「yyyy-MM-ddThh:mm:ss」， 若使用參數「startTime」或「dataTime」，則參數「timeFrom」的篩選資料則會失效，預設為全部回傳"
          },
          {
            "name": "timeTo",
            "required": False,
            "type": "string($date-time)",
            "description": "時間區段，篩選需要之時間區段，時間從內容之最初時間開始篩選，直到 「timeTo」，並可與參數 「timeFrom」 合併使用，格式為「yyyy-MM-ddThh:mm:ss」，使用「startTime」或「dataTime」，則參數「timeTo」的篩選資料則會失效，預設為全部回傳"
          }
        ]
      },
      {
        "path": "/v1/rest/datastore/F-D0047-049",
        "dataId": "F-D0047-049",
        "summary": "鄉鎮天氣預報-基隆市未來2天天氣預報",
        "description": "臺灣各鄉鎮市區預報資料-臺灣各鄉鎮市區未來2天(逐3小時)及未來1週天氣預報",
        "parameters": [
          {
            "name": "Authorization",
            "required": True,
            "type": "string",
            "description": "氣象開放資料平台會員授權碼"
          },
          {
            "name": "limit",
            "required": False,
            "type": "number($int)",
            "description": "限制最多回傳的資料，預設為回傳全部筆數"
          },
          {
            "name": "offset",
            "required": False,
            "type": "number($int)",
            "description": "指定從第幾筆後開始回傳，預設為第 0 筆開始回傳"
          },
          {
            "name": "format",
            "required": False,
            "type": "string",
            "description": "回傳資料格式，預設為 json 格式Available values: JSON, XML--JSONXML"
          },
          {
            "name": "locationName",
            "required": False,
            "type": "array[string]",
            "description": "各縣市所對應鄉鎮名稱，請參考https://opendata.cwa.gov.tw/opendatadoc/Opendata_City.pdf，附錄 A『全臺縣市鄉鎮對照表』，預設為全部回傳"
          },
          {
            "name": "elementName",
            "required": False,
            "type": "array[string]",
            "description": "天氣預報因子，預設為全部回傳Available values: Wx, PoP12h, AT, T, RH, CI, WeatherDescription, PoP6h, WS, WD, Td--WxPoP12hATTRHCIWeatherDescriptionPoP6hWSWDTd"
          },
          {
            "name": "sort",
            "required": False,
            "type": "string",
            "description": "同時對 「startTime」，「endTime」，「dataTime」 做升冪排序，預設不排序Available values: time--time"
          },
          {
            "name": "startTime",
            "required": False,
            "type": "array[string]",
            "description": "時間因子，格式為「yyyy-MM-ddThh:mm:ss」，預設為全部回傳"
          },
          {
            "name": "dataTime",
            "required": False,
            "type": "array[string]",
            "description": "時間因子，格式為「yyyy-MM-ddThh:mm:ss」，預設為全部回傳"
          },
          {
            "name": "timeFrom",
            "required": False,
            "type": "string($date-time)",
            "description": "時間區段:時間從「timeFrom」 開始篩選，直到內容之最後時間，並可與參數 「timeTo 合併使用，格式為「yyyy-MM-ddThh:mm:ss」， 若使用參數「startTime」或「dataTime」，則參數「timeFrom」的篩選資料則會失效，預設為全部回傳"
          },
          {
            "name": "timeTo",
            "required": False,
            "type": "string($date-time)",
            "description": "時間區段，篩選需要之時間區段，時間從內容之最初時間開始篩選，直到 「timeTo」，並可與參數 「timeFrom」 合併使用，格式為「yyyy-MM-ddThh:mm:ss」，使用「startTime」或「dataTime」，則參數「timeTo」的篩選資料則會失效，預設為全部回傳"
          }
        ]
      },
      {
        "path": "/v1/rest/datastore/F-D0047-051",
        "dataId": "F-D0047-051",
        "summary": "鄉鎮天氣預報-基隆市未來1週天氣預報",
        "description": "臺灣各鄉鎮市區預報資料-臺灣各鄉鎮市區未來2天(逐3小時)及未來1週天氣預報",
        "parameters": [
          {
            "name": "Authorization",
            "required": True,
            "type": "string",
            "description": "氣象開放資料平台會員授權碼"
          },
          {
            "name": "limit",
            "required": False,
            "type": "number($int)",
            "description": "限制最多回傳的資料，預設為回傳全部筆數"
          },
          {
            "name": "offset",
            "required": False,
            "type": "number($int)",
            "description": "指定從第幾筆後開始回傳，預設為第 0 筆開始回傳"
          },
          {
            "name": "format",
            "required": False,
            "type": "string",
            "description": "回傳資料格式，預設為 json 格式Available values: JSON, XML--JSONXML"
          },
          {
            "name": "locationName",
            "required": False,
            "type": "array[string]",
            "description": "各縣市所對應鄉鎮名稱，請參考https://opendata.cwa.gov.tw/opendatadoc/Opendata_City.pdf，附錄 A『全臺縣市鄉鎮對照表』，預設為全部回傳"
          },
          {
            "name": "elementName",
            "required": False,
            "type": "array[string]",
            "description": "天氣預報因子，預設為全部回傳Available values: MinCI, MaxAT, MaxCI, MinT, UVI, MinAT, MaxT, WS, WD, Td, PoP12h, T, RH, Wx, WeatherDescription--MinCIMaxATMaxCIMinTUVIMinATMaxTWSWDTdPoP12hTRHWxWeatherDescription"
          },
          {
            "name": "sort",
            "required": False,
            "type": "string",
            "description": "同時對 「startTime」，「endTime」，「dataTime」 做升冪排序，預設不排序Available values: time--time"
          },
          {
            "name": "startTime",
            "required": False,
            "type": "array[string]",
            "description": "時間因子，格式為「yyyy-MM-ddThh:mm:ss」，預設為全部回傳"
          },
          {
            "name": "dataTime",
            "required": False,
            "type": "array[string]",
            "description": "時間因子，格式為「yyyy-MM-ddThh:mm:ss」，預設為全部回傳"
          },
          {
            "name": "timeFrom",
            "required": False,
            "type": "string($date-time)",
            "description": "時間區段:時間從「timeFrom」 開始篩選，直到內容之最後時間，並可與參數 「timeTo 合併使用，格式為「yyyy-MM-ddThh:mm:ss」， 若使用參數「startTime」或「dataTime」，則參數「timeFrom」的篩選資料則會失效，預設為全部回傳"
          },
          {
            "name": "timeTo",
            "required": False,
            "type": "string($date-time)",
            "description": "時間區段，篩選需要之時間區段，時間從內容之最初時間開始篩選，直到 「timeTo」，並可與參數 「timeFrom」 合併使用，格式為「yyyy-MM-ddThh:mm:ss」，使用「startTime」或「dataTime」，則參數「timeTo」的篩選資料則會失效，預設為全部回傳"
          }
        ]
      },
      {
        "path": "/v1/rest/datastore/F-D0047-053",
        "dataId": "F-D0047-053",
        "summary": "鄉鎮天氣預報-新竹市未來2天天氣預報",
        "description": "臺灣各鄉鎮市區預報資料-臺灣各鄉鎮市區未來2天(逐3小時)及未來1週天氣預報",
        "parameters": [
          {
            "name": "Authorization",
            "required": True,
            "type": "string",
            "description": "氣象開放資料平台會員授權碼"
          },
          {
            "name": "limit",
            "required": False,
            "type": "number($int)",
            "description": "限制最多回傳的資料，預設為回傳全部筆數"
          },
          {
            "name": "offset",
            "required": False,
            "type": "number($int)",
            "description": "指定從第幾筆後開始回傳，預設為第 0 筆開始回傳"
          },
          {
            "name": "format",
            "required": False,
            "type": "string",
            "description": "回傳資料格式，預設為 json 格式Available values: JSON, XML--JSONXML"
          },
          {
            "name": "locationName",
            "required": False,
            "type": "array[string]",
            "description": "各縣市所對應鄉鎮名稱，請參考https://opendata.cwa.gov.tw/opendatadoc/Opendata_City.pdf，附錄 A『全臺縣市鄉鎮對照表』，預設為全部回傳"
          },
          {
            "name": "elementName",
            "required": False,
            "type": "array[string]",
            "description": "天氣預報因子，預設為全部回傳Available values: Wx, PoP12h, AT, T, RH, CI, WeatherDescription, PoP6h, WS, WD, Td--WxPoP12hATTRHCIWeatherDescriptionPoP6hWSWDTd"
          },
          {
            "name": "sort",
            "required": False,
            "type": "string",
            "description": "同時對 「startTime」，「endTime」，「dataTime」 做升冪排序，預設不排序Available values: time--time"
          },
          {
            "name": "startTime",
            "required": False,
            "type": "array[string]",
            "description": "時間因子，格式為「yyyy-MM-ddThh:mm:ss」，預設為全部回傳"
          },
          {
            "name": "dataTime",
            "required": False,
            "type": "array[string]",
            "description": "時間因子，格式為「yyyy-MM-ddThh:mm:ss」，預設為全部回傳"
          },
          {
            "name": "timeFrom",
            "required": False,
            "type": "string($date-time)",
            "description": "時間區段:時間從「timeFrom」 開始篩選，直到內容之最後時間，並可與參數 「timeTo 合併使用，格式為「yyyy-MM-ddThh:mm:ss」， 若使用參數「startTime」或「dataTime」，則參數「timeFrom」的篩選資料則會失效，預設為全部回傳"
          },
          {
            "name": "timeTo",
            "required": False,
            "type": "string($date-time)",
            "description": "時間區段，篩選需要之時間區段，時間從內容之最初時間開始篩選，直到 「timeTo」，並可與參數 「timeFrom」 合併使用，格式為「yyyy-MM-ddThh:mm:ss」，使用「startTime」或「dataTime」，則參數「timeTo」的篩選資料則會失效，預設為全部回傳"
          }
        ]
      },
      {
        "path": "/v1/rest/datastore/F-D0047-055",
        "dataId": "F-D0047-055",
        "summary": "鄉鎮天氣預報-新竹市未來1週天氣預報",
        "description": "臺灣各鄉鎮市區預報資料-臺灣各鄉鎮市區未來2天(逐3小時)及未來1週天氣預報",
        "parameters": [
          {
            "name": "Authorization",
            "required": True,
            "type": "string",
            "description": "氣象開放資料平台會員授權碼"
          },
          {
            "name": "limit",
            "required": False,
            "type": "number($int)",
            "description": "限制最多回傳的資料，預設為回傳全部筆數"
          },
          {
            "name": "offset",
            "required": False,
            "type": "number($int)",
            "description": "指定從第幾筆後開始回傳，預設為第 0 筆開始回傳"
          },
          {
            "name": "format",
            "required": False,
            "type": "string",
            "description": "回傳資料格式，預設為 json 格式Available values: JSON, XML--JSONXML"
          },
          {
            "name": "locationName",
            "required": False,
            "type": "array[string]",
            "description": "各縣市所對應鄉鎮名稱，請參考https://opendata.cwa.gov.tw/opendatadoc/Opendata_City.pdf，附錄 A『全臺縣市鄉鎮對照表』，預設為全部回傳"
          },
          {
            "name": "elementName",
            "required": False,
            "type": "array[string]",
            "description": "天氣預報因子，預設為全部回傳Available values: MinCI, MaxAT, MaxCI, MinT, UVI, MinAT, MaxT, WS, WD, Td, PoP12h, T, RH, Wx, WeatherDescription--MinCIMaxATMaxCIMinTUVIMinATMaxTWSWDTdPoP12hTRHWxWeatherDescription"
          },
          {
            "name": "sort",
            "required": False,
            "type": "string",
            "description": "同時對 「startTime」，「endTime」，「dataTime」 做升冪排序，預設不排序Available values: time--time"
          },
          {
            "name": "startTime",
            "required": False,
            "type": "array[string]",
            "description": "時間因子，格式為「yyyy-MM-ddThh:mm:ss」，預設為全部回傳"
          },
          {
            "name": "dataTime",
            "required": False,
            "type": "array[string]",
            "description": "時間因子，格式為「yyyy-MM-ddThh:mm:ss」，預設為全部回傳"
          },
          {
            "name": "timeFrom",
            "required": False,
            "type": "string($date-time)",
            "description": "時間區段:時間從「timeFrom」 開始篩選，直到內容之最後時間，並可與參數 「timeTo 合併使用，格式為「yyyy-MM-ddThh:mm:ss」， 若使用參數「startTime」或「dataTime」，則參數「timeFrom」的篩選資料則會失效，預設為全部回傳"
          },
          {
            "name": "timeTo",
            "required": False,
            "type": "string($date-time)",
            "description": "時間區段，篩選需要之時間區段，時間從內容之最初時間開始篩選，直到 「timeTo」，並可與參數 「timeFrom」 合併使用，格式為「yyyy-MM-ddThh:mm:ss」，使用「startTime」或「dataTime」，則參數「timeTo」的篩選資料則會失效，預設為全部回傳"
          }
        ]
      },
      {
        "path": "/v1/rest/datastore/F-D0047-057",
        "dataId": "F-D0047-057",
        "summary": "鄉鎮天氣預報-嘉義市未來2天天氣預報",
        "description": "臺灣各鄉鎮市區預報資料-臺灣各鄉鎮市區未來2天(逐3小時)及未來1週天氣預報",
        "parameters": [
          {
            "name": "Authorization",
            "required": True,
            "type": "string",
            "description": "氣象開放資料平台會員授權碼"
          },
          {
            "name": "limit",
            "required": False,
            "type": "number($int)",
            "description": "限制最多回傳的資料，預設為回傳全部筆數"
          },
          {
            "name": "offset",
            "required": False,
            "type": "number($int)",
            "description": "指定從第幾筆後開始回傳，預設為第 0 筆開始回傳"
          },
          {
            "name": "format",
            "required": False,
            "type": "string",
            "description": "回傳資料格式，預設為 json 格式Available values: JSON, XML--JSONXML"
          },
          {
            "name": "locationName",
            "required": False,
            "type": "array[string]",
            "description": "各縣市所對應鄉鎮名稱，請參考https://opendata.cwa.gov.tw/opendatadoc/Opendata_City.pdf，附錄 A『全臺縣市鄉鎮對照表』，預設為全部回傳"
          },
          {
            "name": "elementName",
            "required": False,
            "type": "array[string]",
            "description": "天氣預報因子，預設為全部回傳Available values: Wx, PoP12h, AT, T, RH, CI, WeatherDescription, PoP6h, WS, WD, Td--WxPoP12hATTRHCIWeatherDescriptionPoP6hWSWDTd"
          },
          {
            "name": "sort",
            "required": False,
            "type": "string",
            "description": "同時對 「startTime」，「endTime」，「dataTime」 做升冪排序，預設不排序Available values: time--time"
          },
          {
            "name": "startTime",
            "required": False,
            "type": "array[string]",
            "description": "時間因子，格式為「yyyy-MM-ddThh:mm:ss」，預設為全部回傳"
          },
          {
            "name": "dataTime",
            "required": False,
            "type": "array[string]",
            "description": "時間因子，格式為「yyyy-MM-ddThh:mm:ss」，預設為全部回傳"
          },
          {
            "name": "timeFrom",
            "required": False,
            "type": "string($date-time)",
            "description": "時間區段:時間從「timeFrom」 開始篩選，直到內容之最後時間，並可與參數 「timeTo 合併使用，格式為「yyyy-MM-ddThh:mm:ss」， 若使用參數「startTime」或「dataTime」，則參數「timeFrom」的篩選資料則會失效，預設為全部回傳"
          },
          {
            "name": "timeTo",
            "required": False,
            "type": "string($date-time)",
            "description": "時間區段，篩選需要之時間區段，時間從內容之最初時間開始篩選，直到 「timeTo」，並可與參數 「timeFrom」 合併使用，格式為「yyyy-MM-ddThh:mm:ss」，使用「startTime」或「dataTime」，則參數「timeTo」的篩選資料則會失效，預設為全部回傳"
          }
        ]
      },
      {
        "path": "/v1/rest/datastore/F-D0047-059",
        "dataId": "F-D0047-059",
        "summary": "鄉鎮天氣預報-嘉義市未來1週天氣預報",
        "description": "臺灣各鄉鎮市區預報資料-臺灣各鄉鎮市區未來2天(逐3小時)及未來1週天氣預報",
        "parameters": [
          {
            "name": "Authorization",
            "required": True,
            "type": "string",
            "description": "氣象開放資料平台會員授權碼"
          },
          {
            "name": "limit",
            "required": False,
            "type": "number($int)",
            "description": "限制最多回傳的資料，預設為回傳全部筆數"
          },
          {
            "name": "offset",
            "required": False,
            "type": "number($int)",
            "description": "指定從第幾筆後開始回傳，預設為第 0 筆開始回傳"
          },
          {
            "name": "format",
            "required": False,
            "type": "string",
            "description": "回傳資料格式，預設為 json 格式Available values: JSON, XML--JSONXML"
          },
          {
            "name": "locationName",
            "required": False,
            "type": "array[string]",
            "description": "各縣市所對應鄉鎮名稱，請參考https://opendata.cwa.gov.tw/opendatadoc/Opendata_City.pdf，附錄 A『全臺縣市鄉鎮對照表』，預設為全部回傳"
          },
          {
            "name": "elementName",
            "required": False,
            "type": "array[string]",
            "description": "天氣預報因子，預設為全部回傳Available values: MinCI, MaxAT, MaxCI, MinT, UVI, MinAT, MaxT, WS, WD, Td, PoP12h, T, RH, Wx, WeatherDescription--MinCIMaxATMaxCIMinTUVIMinATMaxTWSWDTdPoP12hTRHWxWeatherDescription"
          },
          {
            "name": "sort",
            "required": False,
            "type": "string",
            "description": "同時對 「startTime」，「endTime」，「dataTime」 做升冪排序，預設不排序Available values: time--time"
          },
          {
            "name": "startTime",
            "required": False,
            "type": "array[string]",
            "description": "時間因子，格式為「yyyy-MM-ddThh:mm:ss」，預設為全部回傳"
          },
          {
            "name": "dataTime",
            "required": False,
            "type": "array[string]",
            "description": "時間因子，格式為「yyyy-MM-ddThh:mm:ss」，預設為全部回傳"
          },
          {
            "name": "timeFrom",
            "required": False,
            "type": "string($date-time)",
            "description": "時間區段:時間從「timeFrom」 開始篩選，直到內容之最後時間，並可與參數 「timeTo 合併使用，格式為「yyyy-MM-ddThh:mm:ss」， 若使用參數「startTime」或「dataTime」，則參數「timeFrom」的篩選資料則會失效，預設為全部回傳"
          },
          {
            "name": "timeTo",
            "required": False,
            "type": "string($date-time)",
            "description": "時間區段，篩選需要之時間區段，時間從內容之最初時間開始篩選，直到 「timeTo」，並可與參數 「timeFrom」 合併使用，格式為「yyyy-MM-ddThh:mm:ss」，使用「startTime」或「dataTime」，則參數「timeTo」的篩選資料則會失效，預設為全部回傳"
          }
        ]
      },
      {
        "path": "/v1/rest/datastore/F-D0047-061",
        "dataId": "F-D0047-061",
        "summary": "鄉鎮天氣預報-臺北市未來2天天氣預報",
        "description": "臺灣各鄉鎮市區預報資料-臺灣各鄉鎮市區未來2天(逐3小時)及未來1週天氣預報",
        "parameters": [
          {
            "name": "Authorization",
            "required": True,
            "type": "string",
            "description": "氣象開放資料平台會員授權碼"
          },
          {
            "name": "limit",
            "required": False,
            "type": "number($int)",
            "description": "限制最多回傳的資料，預設為回傳全部筆數"
          },
          {
            "name": "offset",
            "required": False,
            "type": "number($int)",
            "description": "指定從第幾筆後開始回傳，預設為第 0 筆開始回傳"
          },
          {
            "name": "format",
            "required": False,
            "type": "string",
            "description": "回傳資料格式，預設為 json 格式Available values: JSON, XML--JSONXML"
          },
          {
            "name": "locationName",
            "required": False,
            "type": "array[string]",
            "description": "各縣市所對應鄉鎮名稱，請參考https://opendata.cwa.gov.tw/opendatadoc/Opendata_City.pdf，附錄 A『全臺縣市鄉鎮對照表』，預設為全部回傳"
          },
          {
            "name": "elementName",
            "required": False,
            "type": "array[string]",
            "description": "天氣預報因子，預設為全部回傳Available values: Wx, PoP12h, AT, T, RH, CI, WeatherDescription, PoP6h, WS, WD, Td--WxPoP12hATTRHCIWeatherDescriptionPoP6hWSWDTd"
          },
          {
            "name": "sort",
            "required": False,
            "type": "string",
            "description": "同時對 「startTime」，「endTime」，「dataTime」 做升冪排序，預設不排序Available values: time--time"
          },
          {
            "name": "startTime",
            "required": False,
            "type": "array[string]",
            "description": "時間因子，格式為「yyyy-MM-ddThh:mm:ss」，預設為全部回傳"
          },
          {
            "name": "dataTime",
            "required": False,
            "type": "array[string]",
            "description": "時間因子，格式為「yyyy-MM-ddThh:mm:ss」，預設為全部回傳"
          },
          {
            "name": "timeFrom",
            "required": False,
            "type": "string($date-time)",
            "description": "時間區段:時間從「timeFrom」 開始篩選，直到內容之最後時間，並可與參數 「timeTo 合併使用，格式為「yyyy-MM-ddThh:mm:ss」， 若使用參數「startTime」或「dataTime」，則參數「timeFrom」的篩選資料則會失效，預設為全部回傳"
          },
          {
            "name": "timeTo",
            "required": False,
            "type": "string($date-time)",
            "description": "時間區段，篩選需要之時間區段，時間從內容之最初時間開始篩選，直到 「timeTo」，並可與參數 「timeFrom」 合併使用，格式為「yyyy-MM-ddThh:mm:ss」，使用「startTime」或「dataTime」，則參數「timeTo」的篩選資料則會失效，預設為全部回傳"
          }
        ]
      },
      {
        "path": "/v1/rest/datastore/F-D0047-063",
        "dataId": "F-D0047-063",
        "summary": "鄉鎮天氣預報-臺北市未來1週天氣預報",
        "description": "臺灣各鄉鎮市區預報資料-臺灣各鄉鎮市區未來2天(逐3小時)及未來1週天氣預報",
        "parameters": [
          {
            "name": "Authorization",
            "required": True,
            "type": "string",
            "description": "氣象開放資料平台會員授權碼"
          },
          {
            "name": "limit",
            "required": False,
            "type": "number($int)",
            "description": "限制最多回傳的資料，預設為回傳全部筆數"
          },
          {
            "name": "offset",
            "required": False,
            "type": "number($int)",
            "description": "指定從第幾筆後開始回傳，預設為第 0 筆開始回傳"
          },
          {
            "name": "format",
            "required": False,
            "type": "string",
            "description": "回傳資料格式，預設為 json 格式Available values: JSON, XML--JSONXML"
          },
          {
            "name": "locationName",
            "required": False,
            "type": "array[string]",
            "description": "各縣市所對應鄉鎮名稱，請參考https://opendata.cwa.gov.tw/opendatadoc/Opendata_City.pdf，附錄 A『全臺縣市鄉鎮對照表』，預設為全部回傳"
          },
          {
            "name": "elementName",
            "required": False,
            "type": "array[string]",
            "description": "天氣預報因子，預設為全部回傳Available values: MinCI, MaxAT, MaxCI, MinT, UVI, MinAT, MaxT, WS, WD, Td, PoP12h, T, RH, Wx, WeatherDescription--MinCIMaxATMaxCIMinTUVIMinATMaxTWSWDTdPoP12hTRHWxWeatherDescription"
          },
          {
            "name": "sort",
            "required": False,
            "type": "string",
            "description": "同時對 「startTime」，「endTime」，「dataTime」 做升冪排序，預設不排序Available values: time--time"
          },
          {
            "name": "startTime",
            "required": False,
            "type": "array[string]",
            "description": "時間因子，格式為「yyyy-MM-ddThh:mm:ss」，預設為全部回傳"
          },
          {
            "name": "dataTime",
            "required": False,
            "type": "array[string]",
            "description": "時間因子，格式為「yyyy-MM-ddThh:mm:ss」，預設為全部回傳"
          },
          {
            "name": "timeFrom",
            "required": False,
            "type": "string($date-time)",
            "description": "時間區段:時間從「timeFrom」 開始篩選，直到內容之最後時間，並可與參數 「timeTo 合併使用，格式為「yyyy-MM-ddThh:mm:ss」， 若使用參數「startTime」或「dataTime」，則參數「timeFrom」的篩選資料則會失效，預設為全部回傳"
          },
          {
            "name": "timeTo",
            "required": False,
            "type": "string($date-time)",
            "description": "時間區段，篩選需要之時間區段，時間從內容之最初時間開始篩選，直到 「timeTo」，並可與參數 「timeFrom」 合併使用，格式為「yyyy-MM-ddThh:mm:ss」，使用「startTime」或「dataTime」，則參數「timeTo」的篩選資料則會失效，預設為全部回傳"
          }
        ]
      },
      {
        "path": "/v1/rest/datastore/F-D0047-065",
        "dataId": "F-D0047-065",
        "summary": "鄉鎮天氣預報-高雄市未來2天天氣預報",
        "description": "臺灣各鄉鎮市區預報資料-臺灣各鄉鎮市區未來2天(逐3小時)及未來1週天氣預報",
        "parameters": [
          {
            "name": "Authorization",
            "required": True,
            "type": "string",
            "description": "氣象開放資料平台會員授權碼"
          },
          {
            "name": "limit",
            "required": False,
            "type": "number($int)",
            "description": "限制最多回傳的資料，預設為回傳全部筆數"
          },
          {
            "name": "offset",
            "required": False,
            "type": "number($int)",
            "description": "指定從第幾筆後開始回傳，預設為第 0 筆開始回傳"
          },
          {
            "name": "format",
            "required": False,
            "type": "string",
            "description": "回傳資料格式，預設為 json 格式Available values: JSON, XML--JSONXML"
          },
          {
            "name": "locationName",
            "required": False,
            "type": "array[string]",
            "description": "各縣市所對應鄉鎮名稱，請參考https://opendata.cwa.gov.tw/opendatadoc/Opendata_City.pdf，附錄 A『全臺縣市鄉鎮對照表』，預設為全部回傳"
          },
          {
            "name": "elementName",
            "required": False,
            "type": "array[string]",
            "description": "天氣預報因子，預設為全部回傳Available values: Wx, PoP12h, AT, T, RH, CI, WeatherDescription, PoP6h, WS, WD, Td--WxPoP12hATTRHCIWeatherDescriptionPoP6hWSWDTd"
          },
          {
            "name": "sort",
            "required": False,
            "type": "string",
            "description": "同時對 「startTime」，「endTime」，「dataTime」 做升冪排序，預設不排序Available values: time--time"
          },
          {
            "name": "startTime",
            "required": False,
            "type": "array[string]",
            "description": "時間因子，格式為「yyyy-MM-ddThh:mm:ss」，預設為全部回傳"
          },
          {
            "name": "dataTime",
            "required": False,
            "type": "array[string]",
            "description": "時間因子，格式為「yyyy-MM-ddThh:mm:ss」，預設為全部回傳"
          },
          {
            "name": "timeFrom",
            "required": False,
            "type": "string($date-time)",
            "description": "時間區段:時間從「timeFrom」 開始篩選，直到內容之最後時間，並可與參數 「timeTo 合併使用，格式為「yyyy-MM-ddThh:mm:ss」， 若使用參數「startTime」或「dataTime」，則參數「timeFrom」的篩選資料則會失效，預設為全部回傳"
          },
          {
            "name": "timeTo",
            "required": False,
            "type": "string($date-time)",
            "description": "時間區段，篩選需要之時間區段，時間從內容之最初時間開始篩選，直到 「timeTo」，並可與參數 「timeFrom」 合併使用，格式為「yyyy-MM-ddThh:mm:ss」，使用「startTime」或「dataTime」，則參數「timeTo」的篩選資料則會失效，預設為全部回傳"
          }
        ]
      },
      {
        "path": "/v1/rest/datastore/F-D0047-067",
        "dataId": "F-D0047-067",
        "summary": "鄉鎮天氣預報-高雄市未來1週天氣預報",
        "description": "臺灣各鄉鎮市區預報資料-臺灣各鄉鎮市區未來2天(逐3小時)及未來1週天氣預報",
        "parameters": [
          {
            "name": "Authorization",
            "required": True,
            "type": "string",
            "description": "氣象開放資料平台會員授權碼"
          },
          {
            "name": "limit",
            "required": False,
            "type": "number($int)",
            "description": "限制最多回傳的資料，預設為回傳全部筆數"
          },
          {
            "name": "offset",
            "required": False,
            "type": "number($int)",
            "description": "指定從第幾筆後開始回傳，預設為第 0 筆開始回傳"
          },
          {
            "name": "format",
            "required": False,
            "type": "string",
            "description": "回傳資料格式，預設為 json 格式Available values: JSON, XML--JSONXML"
          },
          {
            "name": "locationName",
            "required": False,
            "type": "array[string]",
            "description": "各縣市所對應鄉鎮名稱，請參考https://opendata.cwa.gov.tw/opendatadoc/Opendata_City.pdf，附錄 A『全臺縣市鄉鎮對照表』，預設為全部回傳"
          },
          {
            "name": "elementName",
            "required": False,
            "type": "array[string]",
            "description": "天氣預報因子，預設為全部回傳Available values: MinCI, MaxAT, MaxCI, MinT, UVI, MinAT, MaxT, WS, WD, Td, PoP12h, T, RH, Wx, WeatherDescription--MinCIMaxATMaxCIMinTUVIMinATMaxTWSWDTdPoP12hTRHWxWeatherDescription"
          },
          {
            "name": "sort",
            "required": False,
            "type": "string",
            "description": "同時對 「startTime」，「endTime」，「dataTime」 做升冪排序，預設不排序Available values: time--time"
          },
          {
            "name": "startTime",
            "required": False,
            "type": "array[string]",
            "description": "時間因子，格式為「yyyy-MM-ddThh:mm:ss」，預設為全部回傳"
          },
          {
            "name": "dataTime",
            "required": False,
            "type": "array[string]",
            "description": "時間因子，格式為「yyyy-MM-ddThh:mm:ss」，預設為全部回傳"
          },
          {
            "name": "timeFrom",
            "required": False,
            "type": "string($date-time)",
            "description": "時間區段:時間從「timeFrom」 開始篩選，直到內容之最後時間，並可與參數 「timeTo 合併使用，格式為「yyyy-MM-ddThh:mm:ss」， 若使用參數「startTime」或「dataTime」，則參數「timeFrom」的篩選資料則會失效，預設為全部回傳"
          },
          {
            "name": "timeTo",
            "required": False,
            "type": "string($date-time)",
            "description": "時間區段，篩選需要之時間區段，時間從內容之最初時間開始篩選，直到 「timeTo」，並可與參數 「timeFrom」 合併使用，格式為「yyyy-MM-ddThh:mm:ss」，使用「startTime」或「dataTime」，則參數「timeTo」的篩選資料則會失效，預設為全部回傳"
          }
        ]
      },
      {
        "path": "/v1/rest/datastore/F-D0047-069",
        "dataId": "F-D0047-069",
        "summary": "鄉鎮天氣預報-新北市未來2天天氣預報",
        "description": "臺灣各鄉鎮市區預報資料-臺灣各鄉鎮市區未來2天(逐3小時)及未來1週天氣預報",
        "parameters": [
          {
            "name": "Authorization",
            "required": True,
            "type": "string",
            "description": "氣象開放資料平台會員授權碼"
          },
          {
            "name": "limit",
            "required": False,
            "type": "number($int)",
            "description": "限制最多回傳的資料，預設為回傳全部筆數"
          },
          {
            "name": "offset",
            "required": False,
            "type": "number($int)",
            "description": "指定從第幾筆後開始回傳，預設為第 0 筆開始回傳"
          },
          {
            "name": "format",
            "required": False,
            "type": "string",
            "description": "回傳資料格式，預設為 json 格式Available values: JSON, XML--JSONXML"
          },
          {
            "name": "locationName",
            "required": False,
            "type": "array[string]",
            "description": "各縣市所對應鄉鎮名稱，請參考https://opendata.cwa.gov.tw/opendatadoc/Opendata_City.pdf，附錄 A『全臺縣市鄉鎮對照表』，預設為全部回傳"
          },
          {
            "name": "elementName",
            "required": False,
            "type": "array[string]",
            "description": "天氣預報因子，預設為全部回傳Available values: Wx, PoP12h, AT, T, RH, CI, WeatherDescription, PoP6h, WS, WD, Td--WxPoP12hATTRHCIWeatherDescriptionPoP6hWSWDTd"
          },
          {
            "name": "sort",
            "required": False,
            "type": "string",
            "description": "同時對 「startTime」，「endTime」，「dataTime」 做升冪排序，預設不排序Available values: time--time"
          },
          {
            "name": "startTime",
            "required": False,
            "type": "array[string]",
            "description": "時間因子，格式為「yyyy-MM-ddThh:mm:ss」，預設為全部回傳"
          },
          {
            "name": "dataTime",
            "required": False,
            "type": "array[string]",
            "description": "時間因子，格式為「yyyy-MM-ddThh:mm:ss」，預設為全部回傳"
          },
          {
            "name": "timeFrom",
            "required": False,
            "type": "string($date-time)",
            "description": "時間區段:時間從「timeFrom」 開始篩選，直到內容之最後時間，並可與參數 「timeTo 合併使用，格式為「yyyy-MM-ddThh:mm:ss」， 若使用參數「startTime」或「dataTime」，則參數「timeFrom」的篩選資料則會失效，預設為全部回傳"
          },
          {
            "name": "timeTo",
            "required": False,
            "type": "string($date-time)",
            "description": "時間區段，篩選需要之時間區段，時間從內容之最初時間開始篩選，直到 「timeTo」，並可與參數 「timeFrom」 合併使用，格式為「yyyy-MM-ddThh:mm:ss」，使用「startTime」或「dataTime」，則參數「timeTo」的篩選資料則會失效，預設為全部回傳"
          }
        ]
      },
      {
        "path": "/v1/rest/datastore/F-D0047-071",
        "dataId": "F-D0047-071",
        "summary": "鄉鎮天氣預報-新北市未來1週天氣預報",
        "description": "臺灣各鄉鎮市區預報資料-臺灣各鄉鎮市區未來2天(逐3小時)及未來1週天氣預報",
        "parameters": [
          {
            "name": "Authorization",
            "required": True,
            "type": "string",
            "description": "氣象開放資料平台會員授權碼"
          },
          {
            "name": "limit",
            "required": False,
            "type": "number($int)",
            "description": "限制最多回傳的資料，預設為回傳全部筆數"
          },
          {
            "name": "offset",
            "required": False,
            "type": "number($int)",
            "description": "指定從第幾筆後開始回傳，預設為第 0 筆開始回傳"
          },
          {
            "name": "format",
            "required": False,
            "type": "string",
            "description": "回傳資料格式，預設為 json 格式Available values: JSON, XML--JSONXML"
          },
          {
            "name": "locationName",
            "required": False,
            "type": "array[string]",
            "description": "各縣市所對應鄉鎮名稱，請參考https://opendata.cwa.gov.tw/opendatadoc/Opendata_City.pdf，附錄 A『全臺縣市鄉鎮對照表』，預設為全部回傳"
          },
          {
            "name": "elementName",
            "required": False,
            "type": "array[string]",
            "description": "天氣預報因子，預設為全部回傳Available values: MinCI, MaxAT, MaxCI, MinT, UVI, MinAT, MaxT, WS, WD, Td, PoP12h, T, RH, Wx, WeatherDescription--MinCIMaxATMaxCIMinTUVIMinATMaxTWSWDTdPoP12hTRHWxWeatherDescription"
          },
          {
            "name": "sort",
            "required": False,
            "type": "string",
            "description": "同時對 「startTime」，「endTime」，「dataTime」 做升冪排序，預設不排序Available values: time--time"
          },
          {
            "name": "startTime",
            "required": False,
            "type": "array[string]",
            "description": "時間因子，格式為「yyyy-MM-ddThh:mm:ss」，預設為全部回傳"
          },
          {
            "name": "dataTime",
            "required": False,
            "type": "array[string]",
            "description": "時間因子，格式為「yyyy-MM-ddThh:mm:ss」，預設為全部回傳"
          },
          {
            "name": "timeFrom",
            "required": False,
            "type": "string($date-time)",
            "description": "時間區段:時間從「timeFrom」 開始篩選，直到內容之最後時間，並可與參數 「timeTo 合併使用，格式為「yyyy-MM-ddThh:mm:ss」， 若使用參數「startTime」或「dataTime」，則參數「timeFrom」的篩選資料則會失效，預設為全部回傳"
          },
          {
            "name": "timeTo",
            "required": False,
            "type": "string($date-time)",
            "description": "時間區段，篩選需要之時間區段，時間從內容之最初時間開始篩選，直到 「timeTo」，並可與參數 「timeFrom」 合併使用，格式為「yyyy-MM-ddThh:mm:ss」，使用「startTime」或「dataTime」，則參數「timeTo」的篩選資料則會失效，預設為全部回傳"
          }
        ]
      },
      {
        "path": "/v1/rest/datastore/F-D0047-073",
        "dataId": "F-D0047-073",
        "summary": "鄉鎮天氣預報-臺中市未來2天天氣預報",
        "description": "臺灣各鄉鎮市區預報資料-臺灣各鄉鎮市區未來2天(逐3小時)及未來1週天氣預報",
        "parameters": [
          {
            "name": "Authorization",
            "required": True,
            "type": "string",
            "description": "氣象開放資料平台會員授權碼"
          },
          {
            "name": "limit",
            "required": False,
            "type": "number($int)",
            "description": "限制最多回傳的資料，預設為回傳全部筆數"
          },
          {
            "name": "offset",
            "required": False,
            "type": "number($int)",
            "description": "指定從第幾筆後開始回傳，預設為第 0 筆開始回傳"
          },
          {
            "name": "format",
            "required": False,
            "type": "string",
            "description": "回傳資料格式，預設為 json 格式Available values: JSON, XML--JSONXML"
          },
          {
            "name": "locationName",
            "required": False,
            "type": "array[string]",
            "description": "各縣市所對應鄉鎮名稱，請參考https://opendata.cwa.gov.tw/opendatadoc/Opendata_City.pdf，附錄 A『全臺縣市鄉鎮對照表』，預設為全部回傳"
          },
          {
            "name": "elementName",
            "required": False,
            "type": "array[string]",
            "description": "天氣預報因子，預設為全部回傳Available values: Wx, PoP12h, AT, T, RH, CI, WeatherDescription, PoP6h, WS, WD, Td--WxPoP12hATTRHCIWeatherDescriptionPoP6hWSWDTd"
          },
          {
            "name": "sort",
            "required": False,
            "type": "string",
            "description": "同時對 「startTime」，「endTime」，「dataTime」 做升冪排序，預設不排序Available values: time--time"
          },
          {
            "name": "startTime",
            "required": False,
            "type": "array[string]",
            "description": "時間因子，格式為「yyyy-MM-ddThh:mm:ss」，預設為全部回傳"
          },
          {
            "name": "dataTime",
            "required": False,
            "type": "array[string]",
            "description": "時間因子，格式為「yyyy-MM-ddThh:mm:ss」，預設為全部回傳"
          },
          {
            "name": "timeFrom",
            "required": False,
            "type": "string($date-time)",
            "description": "時間區段:時間從「timeFrom」 開始篩選，直到內容之最後時間，並可與參數 「timeTo 合併使用，格式為「yyyy-MM-ddThh:mm:ss」， 若使用參數「startTime」或「dataTime」，則參數「timeFrom」的篩選資料則會失效，預設為全部回傳"
          },
          {
            "name": "timeTo",
            "required": False,
            "type": "string($date-time)",
            "description": "時間區段，篩選需要之時間區段，時間從內容之最初時間開始篩選，直到 「timeTo」，並可與參數 「timeFrom」 合併使用，格式為「yyyy-MM-ddThh:mm:ss」，使用「startTime」或「dataTime」，則參數「timeTo」的篩選資料則會失效，預設為全部回傳"
          }
        ]
      },
      {
        "path": "/v1/rest/datastore/F-D0047-075",
        "dataId": "F-D0047-075",
        "summary": "鄉鎮天氣預報-臺中市未來1週天氣預報",
        "description": "臺灣各鄉鎮市區預報資料-臺灣各鄉鎮市區未來2天(逐3小時)及未來1週天氣預報",
        "parameters": [
          {
            "name": "Authorization",
            "required": True,
            "type": "string",
            "description": "氣象開放資料平台會員授權碼"
          },
          {
            "name": "limit",
            "required": False,
            "type": "number($int)",
            "description": "限制最多回傳的資料，預設為回傳全部筆數"
          },
          {
            "name": "offset",
            "required": False,
            "type": "number($int)",
            "description": "指定從第幾筆後開始回傳，預設為第 0 筆開始回傳"
          },
          {
            "name": "format",
            "required": False,
            "type": "string",
            "description": "回傳資料格式，預設為 json 格式Available values: JSON, XML--JSONXML"
          },
          {
            "name": "locationName",
            "required": False,
            "type": "array[string]",
            "description": "各縣市所對應鄉鎮名稱，請參考https://opendata.cwa.gov.tw/opendatadoc/Opendata_City.pdf，附錄 A『全臺縣市鄉鎮對照表』，預設為全部回傳"
          },
          {
            "name": "elementName",
            "required": False,
            "type": "array[string]",
            "description": "天氣預報因子，預設為全部回傳Available values: MinCI, MaxAT, MaxCI, MinT, UVI, MinAT, MaxT, WS, WD, Td, PoP12h, T, RH, Wx, WeatherDescription--MinCIMaxATMaxCIMinTUVIMinATMaxTWSWDTdPoP12hTRHWxWeatherDescription"
          },
          {
            "name": "sort",
            "required": False,
            "type": "string",
            "description": "同時對 「startTime」，「endTime」，「dataTime」 做升冪排序，預設不排序Available values: time--time"
          },
          {
            "name": "startTime",
            "required": False,
            "type": "array[string]",
            "description": "時間因子，格式為「yyyy-MM-ddThh:mm:ss」，預設為全部回傳"
          },
          {
            "name": "dataTime",
            "required": False,
            "type": "array[string]",
            "description": "時間因子，格式為「yyyy-MM-ddThh:mm:ss」，預設為全部回傳"
          },
          {
            "name": "timeFrom",
            "required": False,
            "type": "string($date-time)",
            "description": "時間區段:時間從「timeFrom」 開始篩選，直到內容之最後時間，並可與參數 「timeTo 合併使用，格式為「yyyy-MM-ddThh:mm:ss」， 若使用參數「startTime」或「dataTime」，則參數「timeFrom」的篩選資料則會失效，預設為全部回傳"
          },
          {
            "name": "timeTo",
            "required": False,
            "type": "string($date-time)",
            "description": "時間區段，篩選需要之時間區段，時間從內容之最初時間開始篩選，直到 「timeTo」，並可與參數 「timeFrom」 合併使用，格式為「yyyy-MM-ddThh:mm:ss」，使用「startTime」或「dataTime」，則參數「timeTo」的篩選資料則會失效，預設為全部回傳"
          }
        ]
      },
      {
        "path": "/v1/rest/datastore/F-D0047-077",
        "dataId": "F-D0047-077",
        "summary": "鄉鎮天氣預報-臺南市未來2天天氣預報",
        "description": "臺灣各鄉鎮市區預報資料-臺灣各鄉鎮市區未來2天(逐3小時)及未來1週天氣預報",
        "parameters": [
          {
            "name": "Authorization",
            "required": True,
            "type": "string",
            "description": "氣象開放資料平台會員授權碼"
          },
          {
            "name": "limit",
            "required": False,
            "type": "number($int)",
            "description": "限制最多回傳的資料，預設為回傳全部筆數"
          },
          {
            "name": "offset",
            "required": False,
            "type": "number($int)",
            "description": "指定從第幾筆後開始回傳，預設為第 0 筆開始回傳"
          },
          {
            "name": "format",
            "required": False,
            "type": "string",
            "description": "回傳資料格式，預設為 json 格式Available values: JSON, XML--JSONXML"
          },
          {
            "name": "locationName",
            "required": False,
            "type": "array[string]",
            "description": "各縣市所對應鄉鎮名稱，請參考https://opendata.cwa.gov.tw/opendatadoc/Opendata_City.pdf，附錄 A『全臺縣市鄉鎮對照表』，預設為全部回傳"
          },
          {
            "name": "elementName",
            "required": False,
            "type": "array[string]",
            "description": "天氣預報因子，預設為全部回傳Available values: Wx, PoP12h, AT, T, RH, CI, WeatherDescription, PoP6h, WS, WD, Td--WxPoP12hATTRHCIWeatherDescriptionPoP6hWSWDTd"
          },
          {
            "name": "sort",
            "required": False,
            "type": "string",
            "description": "同時對 「startTime」，「endTime」，「dataTime」 做升冪排序，預設不排序Available values: time--time"
          },
          {
            "name": "startTime",
            "required": False,
            "type": "array[string]",
            "description": "時間因子，格式為「yyyy-MM-ddThh:mm:ss」，預設為全部回傳"
          },
          {
            "name": "dataTime",
            "required": False,
            "type": "array[string]",
            "description": "時間因子，格式為「yyyy-MM-ddThh:mm:ss」，預設為全部回傳"
          },
          {
            "name": "timeFrom",
            "required": False,
            "type": "string($date-time)",
            "description": "時間區段:時間從「timeFrom」 開始篩選，直到內容之最後時間，並可與參數 「timeTo 合併使用，格式為「yyyy-MM-ddThh:mm:ss」， 若使用參數「startTime」或「dataTime」，則參數「timeFrom」的篩選資料則會失效，預設為全部回傳"
          },
          {
            "name": "timeTo",
            "required": False,
            "type": "string($date-time)",
            "description": "時間區段，篩選需要之時間區段，時間從內容之最初時間開始篩選，直到 「timeTo」，並可與參數 「timeFrom」 合併使用，格式為「yyyy-MM-ddThh:mm:ss」，使用「startTime」或「dataTime」，則參數「timeTo」的篩選資料則會失效，預設為全部回傳"
          }
        ]
      },
      {
        "path": "/v1/rest/datastore/F-D0047-079",
        "dataId": "F-D0047-079",
        "summary": "鄉鎮天氣預報-臺南市未來1週天氣預報",
        "description": "臺灣各鄉鎮市區預報資料-臺灣各鄉鎮市區未來2天(逐3小時)及未來1週天氣預報",
        "parameters": [
          {
            "name": "Authorization",
            "required": True,
            "type": "string",
            "description": "氣象開放資料平台會員授權碼"
          },
          {
            "name": "limit",
            "required": False,
            "type": "number($int)",
            "description": "限制最多回傳的資料，預設為回傳全部筆數"
          },
          {
            "name": "offset",
            "required": False,
            "type": "number($int)",
            "description": "指定從第幾筆後開始回傳，預設為第 0 筆開始回傳"
          },
          {
            "name": "format",
            "required": False,
            "type": "string",
            "description": "回傳資料格式，預設為 json 格式Available values: JSON, XML--JSONXML"
          },
          {
            "name": "locationName",
            "required": False,
            "type": "array[string]",
            "description": "各縣市所對應鄉鎮名稱，請參考https://opendata.cwa.gov.tw/opendatadoc/Opendata_City.pdf，附錄 A『全臺縣市鄉鎮對照表』，預設為全部回傳"
          },
          {
            "name": "elementName",
            "required": False,
            "type": "array[string]",
            "description": "天氣預報因子，預設為全部回傳Available values: MinCI, MaxAT, MaxCI, MinT, UVI, MinAT, MaxT, WS, WD, Td, PoP12h, T, RH, Wx, WeatherDescription--MinCIMaxATMaxCIMinTUVIMinATMaxTWSWDTdPoP12hTRHWxWeatherDescription"
          },
          {
            "name": "sort",
            "required": False,
            "type": "string",
            "description": "同時對 「startTime」，「endTime」，「dataTime」 做升冪排序，預設不排序Available values: time--time"
          },
          {
            "name": "startTime",
            "required": False,
            "type": "array[string]",
            "description": "時間因子，格式為「yyyy-MM-ddThh:mm:ss」，預設為全部回傳"
          },
          {
            "name": "dataTime",
            "required": False,
            "type": "array[string]",
            "description": "時間因子，格式為「yyyy-MM-ddThh:mm:ss」，預設為全部回傳"
          },
          {
            "name": "timeFrom",
            "required": False,
            "type": "string($date-time)",
            "description": "時間區段:時間從「timeFrom」 開始篩選，直到內容之最後時間，並可與參數 「timeTo 合併使用，格式為「yyyy-MM-ddThh:mm:ss」， 若使用參數「startTime」或「dataTime」，則參數「timeFrom」的篩選資料則會失效，預設為全部回傳"
          },
          {
            "name": "timeTo",
            "required": False,
            "type": "string($date-time)",
            "description": "時間區段，篩選需要之時間區段，時間從內容之最初時間開始篩選，直到 「timeTo」，並可與參數 「timeFrom」 合併使用，格式為「yyyy-MM-ddThh:mm:ss」，使用「startTime」或「dataTime」，則參數「timeTo」的篩選資料則會失效，預設為全部回傳"
          }
        ]
      },
      {
        "path": "/v1/rest/datastore/F-D0047-081",
        "dataId": "F-D0047-081",
        "summary": "鄉鎮天氣預報-連江縣未來2天天氣預報",
        "description": "臺灣各鄉鎮市區預報資料-臺灣各鄉鎮市區未來2天(逐3小時)及未來1週天氣預報",
        "parameters": [
          {
            "name": "Authorization",
            "required": True,
            "type": "string",
            "description": "氣象開放資料平台會員授權碼"
          },
          {
            "name": "limit",
            "required": False,
            "type": "number($int)",
            "description": "限制最多回傳的資料，預設為回傳全部筆數"
          },
          {
            "name": "offset",
            "required": False,
            "type": "number($int)",
            "description": "指定從第幾筆後開始回傳，預設為第 0 筆開始回傳"
          },
          {
            "name": "format",
            "required": False,
            "type": "string",
            "description": "回傳資料格式，預設為 json 格式Available values: JSON, XML--JSONXML"
          },
          {
            "name": "locationName",
            "required": False,
            "type": "array[string]",
            "description": "各縣市所對應鄉鎮名稱，請參考https://opendata.cwa.gov.tw/opendatadoc/Opendata_City.pdf，附錄 A『全臺縣市鄉鎮對照表』，預設為全部回傳"
          },
          {
            "name": "elementName",
            "required": False,
            "type": "array[string]",
            "description": "天氣預報因子，預設為全部回傳Available values: Wx, PoP12h, AT, T, RH, CI, WeatherDescription, PoP6h, WS, WD, Td--WxPoP12hATTRHCIWeatherDescriptionPoP6hWSWDTd"
          },
          {
            "name": "sort",
            "required": False,
            "type": "string",
            "description": "同時對 「startTime」，「endTime」，「dataTime」 做升冪排序，預設不排序Available values: time--time"
          },
          {
            "name": "startTime",
            "required": False,
            "type": "array[string]",
            "description": "時間因子，格式為「yyyy-MM-ddThh:mm:ss」，預設為全部回傳"
          },
          {
            "name": "dataTime",
            "required": False,
            "type": "array[string]",
            "description": "時間因子，格式為「yyyy-MM-ddThh:mm:ss」，預設為全部回傳"
          },
          {
            "name": "timeFrom",
            "required": False,
            "type": "string($date-time)",
            "description": "時間區段:時間從「timeFrom」 開始篩選，直到內容之最後時間，並可與參數 「timeTo 合併使用，格式為「yyyy-MM-ddThh:mm:ss」， 若使用參數「startTime」或「dataTime」，則參數「timeFrom」的篩選資料則會失效，預設為全部回傳"
          },
          {
            "name": "timeTo",
            "required": False,
            "type": "string($date-time)",
            "description": "時間區段，篩選需要之時間區段，時間從內容之最初時間開始篩選，直到 「timeTo」，並可與參數 「timeFrom」 合併使用，格式為「yyyy-MM-ddThh:mm:ss」，使用「startTime」或「dataTime」，則參數「timeTo」的篩選資料則會失效，預設為全部回傳"
          }
        ]
      },
      {
        "path": "/v1/rest/datastore/F-D0047-083",
        "dataId": "F-D0047-083",
        "summary": "鄉鎮天氣預報-連江縣未來1週天氣預報",
        "description": "臺灣各鄉鎮市區預報資料-臺灣各鄉鎮市區未來2天(逐3小時)及未來1週天氣預報",
        "parameters": [
          {
            "name": "Authorization",
            "required": True,
            "type": "string",
            "description": "氣象開放資料平台會員授權碼"
          },
          {
            "name": "limit",
            "required": False,
            "type": "number($int)",
            "description": "限制最多回傳的資料，預設為回傳全部筆數"
          },
          {
            "name": "offset",
            "required": False,
            "type": "number($int)",
            "description": "指定從第幾筆後開始回傳，預設為第 0 筆開始回傳"
          },
          {
            "name": "format",
            "required": False,
            "type": "string",
            "description": "回傳資料格式，預設為 json 格式Available values: JSON, XML--JSONXML"
          },
          {
            "name": "locationName",
            "required": False,
            "type": "array[string]",
            "description": "各縣市所對應鄉鎮名稱，請參考https://opendata.cwa.gov.tw/opendatadoc/Opendata_City.pdf，附錄 A『全臺縣市鄉鎮對照表』，預設為全部回傳"
          },
          {
            "name": "elementName",
            "required": False,
            "type": "array[string]",
            "description": "天氣預報因子，預設為全部回傳Available values: MinCI, MaxAT, MaxCI, MinT, UVI, MinAT, MaxT, WS, WD, Td, PoP12h, T, RH, Wx, WeatherDescription--MinCIMaxATMaxCIMinTUVIMinATMaxTWSWDTdPoP12hTRHWxWeatherDescription"
          },
          {
            "name": "sort",
            "required": False,
            "type": "string",
            "description": "同時對 「startTime」，「endTime」，「dataTime」 做升冪排序，預設不排序Available values: time--time"
          },
          {
            "name": "startTime",
            "required": False,
            "type": "array[string]",
            "description": "時間因子，格式為「yyyy-MM-ddThh:mm:ss」，預設為全部回傳"
          },
          {
            "name": "dataTime",
            "required": False,
            "type": "array[string]",
            "description": "時間因子，格式為「yyyy-MM-ddThh:mm:ss」，預設為全部回傳"
          },
          {
            "name": "timeFrom",
            "required": False,
            "type": "string($date-time)",
            "description": "時間區段:時間從「timeFrom」 開始篩選，直到內容之最後時間，並可與參數 「timeTo 合併使用，格式為「yyyy-MM-ddThh:mm:ss」， 若使用參數「startTime」或「dataTime」，則參數「timeFrom」的篩選資料則會失效，預設為全部回傳"
          },
          {
            "name": "timeTo",
            "required": False,
            "type": "string($date-time)",
            "description": "時間區段，篩選需要之時間區段，時間從內容之最初時間開始篩選，直到 「timeTo」，並可與參數 「timeFrom」 合併使用，格式為「yyyy-MM-ddThh:mm:ss」，使用「startTime」或「dataTime」，則參數「timeTo」的篩選資料則會失效，預設為全部回傳"
          }
        ]
      },
      {
        "path": "/v1/rest/datastore/F-D0047-085",
        "dataId": "F-D0047-085",
        "summary": "鄉鎮天氣預報-金門縣未來2天天氣預報",
        "description": "臺灣各鄉鎮市區預報資料-臺灣各鄉鎮市區未來2天(逐3小時)及未來1週天氣預報",
        "parameters": [
          {
            "name": "Authorization",
            "required": True,
            "type": "string",
            "description": "氣象開放資料平台會員授權碼"
          },
          {
            "name": "limit",
            "required": False,
            "type": "number($int)",
            "description": "限制最多回傳的資料，預設為回傳全部筆數"
          },
          {
            "name": "offset",
            "required": False,
            "type": "number($int)",
            "description": "指定從第幾筆後開始回傳，預設為第 0 筆開始回傳"
          },
          {
            "name": "format",
            "required": False,
            "type": "string",
            "description": "回傳資料格式，預設為 json 格式Available values: JSON, XML--JSONXML"
          },
          {
            "name": "locationName",
            "required": False,
            "type": "array[string]",
            "description": "各縣市所對應鄉鎮名稱，請參考https://opendata.cwa.gov.tw/opendatadoc/Opendata_City.pdf，附錄 A『全臺縣市鄉鎮對照表』，預設為全部回傳"
          },
          {
            "name": "elementName",
            "required": False,
            "type": "array[string]",
            "description": "天氣預報因子，預設為全部回傳Available values: Wx, PoP12h, AT, T, RH, CI, WeatherDescription, PoP6h, WS, WD, Td--WxPoP12hATTRHCIWeatherDescriptionPoP6hWSWDTd"
          },
          {
            "name": "sort",
            "required": False,
            "type": "string",
            "description": "同時對 「startTime」，「endTime」，「dataTime」 做升冪排序，預設不排序Available values: time--time"
          },
          {
            "name": "startTime",
            "required": False,
            "type": "array[string]",
            "description": "時間因子，格式為「yyyy-MM-ddThh:mm:ss」，預設為全部回傳"
          },
          {
            "name": "dataTime",
            "required": False,
            "type": "array[string]",
            "description": "時間因子，格式為「yyyy-MM-ddThh:mm:ss」，預設為全部回傳"
          },
          {
            "name": "timeFrom",
            "required": False,
            "type": "string($date-time)",
            "description": "時間區段:時間從「timeFrom」 開始篩選，直到內容之最後時間，並可與參數 「timeTo 合併使用，格式為「yyyy-MM-ddThh:mm:ss」， 若使用參數「startTime」或「dataTime」，則參數「timeFrom」的篩選資料則會失效，預設為全部回傳"
          },
          {
            "name": "timeTo",
            "required": False,
            "type": "string($date-time)",
            "description": "時間區段，篩選需要之時間區段，時間從內容之最初時間開始篩選，直到 「timeTo」，並可與參數 「timeFrom」 合併使用，格式為「yyyy-MM-ddThh:mm:ss」，使用「startTime」或「dataTime」，則參數「timeTo」的篩選資料則會失效，預設為全部回傳"
          }
        ]
      },
      {
        "path": "/v1/rest/datastore/F-D0047-087",
        "dataId": "F-D0047-087",
        "summary": "鄉鎮天氣預報-金門縣未來1週天氣預報",
        "description": "臺灣各鄉鎮市區預報資料-臺灣各鄉鎮市區未來2天(逐3小時)及未來1週天氣預報",
        "parameters": [
          {
            "name": "Authorization",
            "required": True,
            "type": "string",
            "description": "氣象開放資料平台會員授權碼"
          },
          {
            "name": "limit",
            "required": False,
            "type": "number($int)",
            "description": "限制最多回傳的資料，預設為回傳全部筆數"
          },
          {
            "name": "offset",
            "required": False,
            "type": "number($int)",
            "description": "指定從第幾筆後開始回傳，預設為第 0 筆開始回傳"
          },
          {
            "name": "format",
            "required": False,
            "type": "string",
            "description": "回傳資料格式，預設為 json 格式Available values: JSON, XML--JSONXML"
          },
          {
            "name": "locationName",
            "required": False,
            "type": "array[string]",
            "description": "各縣市所對應鄉鎮名稱，請參考https://opendata.cwa.gov.tw/opendatadoc/Opendata_City.pdf，附錄 A『全臺縣市鄉鎮對照表』，預設為全部回傳"
          },
          {
            "name": "elementName",
            "required": False,
            "type": "array[string]",
            "description": "天氣預報因子，預設為全部回傳Available values: MinCI, MaxAT, MaxCI, MinT, UVI, MinAT, MaxT, WS, WD, Td, PoP12h, T, RH, Wx, WeatherDescription--MinCIMaxATMaxCIMinTUVIMinATMaxTWSWDTdPoP12hTRHWxWeatherDescription"
          },
          {
            "name": "sort",
            "required": False,
            "type": "string",
            "description": "同時對 「startTime」，「endTime」，「dataTime」 做升冪排序，預設不排序Available values: time--time"
          },
          {
            "name": "startTime",
            "required": False,
            "type": "array[string]",
            "description": "時間因子，格式為「yyyy-MM-ddThh:mm:ss」，預設為全部回傳"
          },
          {
            "name": "dataTime",
            "required": False,
            "type": "array[string]",
            "description": "時間因子，格式為「yyyy-MM-ddThh:mm:ss」，預設為全部回傳"
          },
          {
            "name": "timeFrom",
            "required": False,
            "type": "string($date-time)",
            "description": "時間區段:時間從「timeFrom」 開始篩選，直到內容之最後時間，並可與參數 「timeTo 合併使用，格式為「yyyy-MM-ddThh:mm:ss」， 若使用參數「startTime」或「dataTime」，則參數「timeFrom」的篩選資料則會失效，預設為全部回傳"
          },
          {
            "name": "timeTo",
            "required": False,
            "type": "string($date-time)",
            "description": "時間區段，篩選需要之時間區段，時間從內容之最初時間開始篩選，直到 「timeTo」，並可與參數 「timeFrom」 合併使用，格式為「yyyy-MM-ddThh:mm:ss」，使用「startTime」或「dataTime」，則參數「timeTo」的篩選資料則會失效，預設為全部回傳"
          }
        ]
      },
      {
        "path": "/v1/rest/datastore/F-D0047-089",
        "dataId": "F-D0047-089",
        "summary": "鄉鎮天氣預報-臺灣未來 2 天天氣預報",
        "description": "臺灣各鄉鎮市區預報資料-臺灣各鄉鎮市區未來2天(逐3小時)",
        "parameters": [
          {
            "name": "Authorization",
            "required": True,
            "type": "string",
            "description": "氣象開放資料平台會員授權碼"
          },
          {
            "name": "limit",
            "required": False,
            "type": "number($int)",
            "description": "限制最多回傳的資料，預設為回傳全部筆數"
          },
          {
            "name": "offset",
            "required": False,
            "type": "number($int)",
            "description": "指定從第幾筆後開始回傳，預設為第 0 筆開始回傳"
          },
          {
            "name": "format",
            "required": False,
            "type": "string",
            "description": "回傳資料格式，預設為 json 格式Available values: JSON, XML--JSONXML"
          },
          {
            "name": "locationName",
            "required": False,
            "type": "array[string]",
            "description": "臺灣各縣市，預設為回傳全部縣市Available values: 宜蘭縣, 花蓮縣, 臺東縣, 澎湖縣, 金門縣, 連江縣, 臺北市, 新北市, 桃園市, 臺中市, 臺南市, 高雄市, 基隆市, 新竹縣, 新竹市, 苗栗縣, 彰化縣, 南投縣, 雲林縣, 嘉義縣, 嘉義市, 屏東縣--宜蘭縣花蓮縣臺東縣澎湖縣金門縣連江縣臺北市新北市桃園市臺中市臺南市高雄市基隆市新竹縣新竹市苗栗縣彰化縣南投縣雲林縣嘉義縣嘉義市屏東縣"
          },
          {
            "name": "elementName",
            "required": False,
            "type": "array[string]",
            "description": "天氣預報因子，預設為全部回傳Available values: Wx, PoP12h, AT, T, RH, CI, WeatherDescription, PoP6h, WS, WD, Td--WxPoP12hATTRHCIWeatherDescriptionPoP6hWSWDTd"
          },
          {
            "name": "sort",
            "required": False,
            "type": "string",
            "description": "同時對 「startTime」、「endTime」、「dataTime」 做升冪排序，預設不排序Available values: time--time"
          },
          {
            "name": "startTime",
            "required": False,
            "type": "array[string]",
            "description": "時間因子，格式為「yyyy-MM-ddThh:mm:ss」，預設為全部回傳"
          },
          {
            "name": "dataTime",
            "required": False,
            "type": "array[string]",
            "description": "時間因子，格式為「yyyy-MM-ddThh:mm:ss」，預設為全部回傳"
          },
          {
            "name": "timeFrom",
            "required": False,
            "type": "string($date-time)",
            "description": "時間區段，篩選需要之時間區段，時間從「timeFrom」 開始篩選，直到內容之最後時間，並可與參數 「timeTo」 合併使用，格式為「yyyy-MM-ddThh:mm:ss」，若使用參數「startTime」或「dataTime」，則參數「timeFrom」的篩選資料則會失效，預設為全部回傳"
          },
          {
            "name": "timeTo",
            "required": False,
            "type": "string($date-time)",
            "description": "時間區段，篩選需要之時間區段，時間從內容之最初時間開始篩選，直到 timeTo，並可與參數 「timeFrom」 合併使用，格式為「yyyy-MM-ddThh:mm:ss」，若使用「startTime」或「dataTime」，則參數「timeTo」的篩選資料則會失效，預設為全部回傳"
          }
        ]
      },
      {
        "path": "/v1/rest/datastore/F-D0047-091",
        "dataId": "F-D0047-091",
        "summary": "鄉鎮天氣預報-臺灣未來1週天氣預報",
        "description": "臺灣各鄉鎮市區預報資料-臺灣各鄉鎮市區未來1週天氣預報",
        "parameters": [
          {
            "name": "Authorization",
            "required": True,
            "type": "string",
            "description": "氣象開放資料平台會員授權碼"
          },
          {
            "name": "limit",
            "required": False,
            "type": "number($int)",
            "description": "限制最多回傳的資料，預設為回傳全部筆數"
          },
          {
            "name": "offset",
            "required": False,
            "type": "number($int)",
            "description": "指定從第幾筆後開始回傳，預設為第 0 筆開始回傳"
          },
          {
            "name": "format",
            "required": False,
            "type": "string",
            "description": "回傳資料格式，預設為 json 格式Available values: JSON, XML--JSONXML"
          },
          {
            "name": "locationName",
            "required": False,
            "type": "array[string]",
            "description": "臺灣各縣市Available values: 宜蘭縣, 花蓮縣, 臺東縣, 澎湖縣, 金門縣, 連江縣, 臺北市, 新北市, 桃園市, 臺中市, 臺南市, 高雄市, 基隆市, 新竹縣, 新竹市, 苗栗縣, 彰化縣, 南投縣, 雲林縣, 嘉義縣, 嘉義市, 屏東縣--宜蘭縣花蓮縣臺東縣澎湖縣金門縣連江縣臺北市新北市桃園市臺中市臺南市高雄市基隆市新竹縣新竹市苗栗縣彰化縣南投縣雲林縣嘉義縣嘉義市屏東縣"
          },
          {
            "name": "elementName",
            "required": False,
            "type": "array[string]",
            "description": "天氣預報因子，預設為全部回傳Available values: MinCI, MaxAT, MaxCI, MinT, UVI, MinAT, MaxT, WS, WD, Td, PoP12h, T, RH, Wx, WeatherDescription--MinCIMaxATMaxCIMinTUVIMinATMaxTWSWDTdPoP12hTRHWxWeatherDescription"
          },
          {
            "name": "sort",
            "required": False,
            "type": "string",
            "description": "同時對 「startTime」，「endTime」，「dataTime」 做升冪排序，預設不排序Available values: time--time"
          },
          {
            "name": "startTime",
            "required": False,
            "type": "array[string]",
            "description": "時間因子，格式為「yyyy-MM-ddThh:mm:ss」，預設為全部回傳"
          },
          {
            "name": "dataTime",
            "required": False,
            "type": "array[string]",
            "description": "時間因子，格式為「yyyy-MM-ddThh:mm:ss」，預設為全部回傳"
          },
          {
            "name": "timeFrom",
            "required": False,
            "type": "string($date-time)",
            "description": "時間區段，篩選需要之時間區段，時間從「timeFrom」 開始篩選，直到內容之最後時間，並可與參數 「timeTo」 合併使用，格式為「yyyy-MM-ddThh:mm:ss」，若使用參數「startTime」或「dataTime」，則參數「timeFrom」的篩選資料則會失效，預設為全部回傳"
          },
          {
            "name": "timeTo",
            "required": False,
            "type": "string($date-time)",
            "description": "時間區段，篩選需要之時間區段，時間從內容之最初時間開始篩選，直到 timeTo，並可與參數 「timeFrom」 合併使用，格式為「yyyy-MM-ddThh:mm:ss」，若使用「startTime」或「dataTime」，則參數「timeTo」的篩選資料則會失效，預設為全部回傳"
          }
        ]
      },
      {
        "path": "/v1/rest/datastore/F-D0047-093",
        "dataId": "F-D0047-093",
        "summary": "鄉鎮天氣預報-全臺灣各鄉鎮市區預報資料",
        "description": "鄉鎮天氣預報可跨縣市截取單一鄉鎮市區預報資料因應系統負載最多一次可擷取 5 個指定縣市之單一鄉鎮市區預報資料，最少1 個指定縣市之單一鄉鎮市區預報資料。",
        "parameters": [
          {
            "name": "Authorization",
            "required": True,
            "type": "string",
            "description": "氣象開放資料平台會員授權碼"
          },
          {
            "name": "limit",
            "required": False,
            "type": "number($int)",
            "description": "限制最多回傳的資料，預設為回傳全部筆數"
          },
          {
            "name": "offset",
            "required": False,
            "type": "number($int)",
            "description": "指定從第幾筆後開始回傳，預設為第 0 筆開始回傳"
          },
          {
            "name": "format",
            "required": False,
            "type": "string",
            "description": "回傳資料格式，預設為 json 格式Available values: JSON, XML--JSONXML"
          },
          {
            "name": "locationId",
            "required": True,
            "type": "array[string]",
            "description": "單一鄉鎮市區預報資料之資料項編號:F-D0047-001至F-D0047-091(單號)，最多五個欄位，最少一個欄位Available values: F-D0047-001, F-D0047-003, F-D0047-005, F-D0047-007, F-D0047-009, F-D0047-011, F-D0047-013, F-D0047-015, F-D0047-017, F-D0047-019, F-D0047-021, F-D0047-023, F-D0047-025, F-D0047-027, F-D0047-029, F-D0047-031, F-D0047-033, F-D0047-035, F-D0047-037, F-D0047-039, F-D0047-041, F-D0047-043, F-D0047-045, F-D0047-047, F-D0047-049, F-D0047-051, F-D0047-053, F-D0047-055, F-D0047-057, F-D0047-059, F-D0047-061, F-D0047-063, F-D0047-065, F-D0047-067, F-D0047-069, F-D0047-071, F-D0047-073, F-D0047-075, F-D0047-077, F-D0047-079, F-D0047-081, F-D0047-083, F-D0047-085, F-D0047-087, F-D0047-089, F-D0047-091F-D0047-001F-D0047-003F-D0047-005F-D0047-007F-D0047-009F-D0047-011F-D0047-013F-D0047-015F-D0047-017F-D0047-019F-D0047-021F-D0047-023F-D0047-025F-D0047-027F-D0047-029F-D0047-031F-D0047-033F-D0047-035F-D0047-037F-D0047-039F-D0047-041F-D0047-043F-D0047-045F-D0047-047F-D0047-049F-D0047-051F-D0047-053F-D0047-055F-D0047-057F-D0047-059F-D0047-061F-D0047-063F-D0047-065F-D0047-067F-D0047-069F-D0047-071F-D0047-073F-D0047-075F-D0047-077F-D0047-079F-D0047-081F-D0047-083F-D0047-085F-D0047-087F-D0047-089F-D0047-091"
          },
          {
            "name": "locationName",
            "required": False,
            "type": "array[string]",
            "description": "各縣市所對應鄉鎮名稱，請詳https://opendata.cwa.gov.tw/opendatadoc/Opendata_City.pdf附錄 A『全臺縣市鄉鎮對照表』"
          },
          {
            "name": "elementName",
            "required": False,
            "type": "array[string]",
            "description": "天氣預報天氣因子，可以接受2天天氣預報天氣因子及1週天氣預報天氣因子。預設為所輸入各個locationId 對應的所有欄位。Available values: AT, CI, PoP6h, MinCI, MaxAT, MaxCI, MinT, UVI, MinAT, MaxT, WS, WD, Td, PoP12h, T, RH, Wx, WeatherDescription--ATCIPoP6hMinCIMaxATMaxCIMinTUVIMinATMaxTWSWDTdPoP12hTRHWxWeatherDescription"
          },
          {
            "name": "sort",
            "required": False,
            "type": "string",
            "description": "同時對 「startTime」，「endTime」，「dataTime」 做升冪排序，預設不排序Available values: time--time"
          },
          {
            "name": "startTime",
            "required": False,
            "type": "array[string]",
            "description": "時間因子，格式為「yyyy-MM-ddThh:mm:ss」，預設為全部回傳"
          },
          {
            "name": "dataTime",
            "required": False,
            "type": "array[string]",
            "description": "時間因子，格式為「yyyy-MM-ddThh:mm:ss」，預設為全部回傳"
          },
          {
            "name": "timeFrom",
            "required": False,
            "type": "string($date-time)",
            "description": "時間區段，篩選需要之時間區段，時間從「timeFrom」 開始篩選，直到內容之最後時間，並可與參數 「timeTo」 合併使用，格式為「yyyy-MM-ddThh:mm:ss」，若使用參數「startTime」或「dataTime」，則參數「timeFrom」的篩選資料則會失效，預設為全部回傳"
          },
          {
            "name": "timeTo",
            "required": False,
            "type": "string($date-time)",
            "description": "時間區段，篩選需要之時間區段，時間從內容之最初時間開始篩選，直到 timeTo，並可與參數 「timeFrom」 合併使用，格式為「yyyy-MM-ddThh:mm:ss」，若使用「startTime」或「dataTime」，則參數「timeTo」的篩選資料則會失效，預設為全部回傳"
          }
        ]
      },
      {
        "path": "/v1/rest/datastore/F-A0021-001",
        "dataId": "F-A0021-001",
        "summary": "潮汐預報-未來 1 個月潮汐預報",
        "description": "未來1個月潮汐預報",
        "parameters": [
          {
            "name": "Authorization",
            "required": True,
            "type": "string",
            "description": "氣象開放資料平台會員授權碼"
          },
          {
            "name": "limit",
            "required": False,
            "type": "number($int)",
            "description": "限制最多回傳的資料，預設為回傳全部筆數"
          },
          {
            "name": "offset",
            "required": False,
            "type": "number($int)",
            "description": "指定從第幾筆後開始回傳，預設為第 0 筆開始回傳"
          },
          {
            "name": "format",
            "required": False,
            "type": "string",
            "description": "回傳資料格式，預設為 json 格式Available values: JSON, XML--JSONXML"
          },
          {
            "name": "LocationName",
            "required": False,
            "type": "array[string]",
            "description": "地點，請參考https://opendata.cwa.gov.tw/opendatadoc/MMC/A0021-001.pdf，若使用參數「LocationId」，則參數「LocationName」的篩選會失效，預設為全部回傳"
          },
          {
            "name": "LocationId",
            "required": False,
            "type": "array[string]",
            "description": "地點，請參考https://opendata.cwa.gov.tw/opendatadoc/MMC/A0021-001.pdf，預設為全部回傳"
          },
          {
            "name": "WeatherElement",
            "required": False,
            "type": "array[string]",
            "description": "氣象因子，預設為全部回傳；若未選擇Tide或TideHeight，Time就不顯示Available values: LunarDate, TideRange, Tide, TideHeights--LunarDateTideRangeTideTideHeights"
          },
          {
            "name": "TideRange",
            "required": False,
            "type": "array[string]",
            "description": "潮差，預設為全部回傳Available values: 大, 中, 小--大中小"
          },
          {
            "name": "sort",
            "required": False,
            "type": "array[string]",
            "description": "「Date」 為針對「Date」做排序，「DateTime」 為針對 「DateTime」 做排序，預設不排序Available values: Date, DateTime--DateDateTime"
          },
          {
            "name": "Date",
            "required": False,
            "type": "array[string]",
            "description": "預報時間因子，日期，格式為「yyyy-MM-dd」，預設為全部回傳"
          },
          {
            "name": "hhmmss",
            "required": False,
            "type": "array[string]",
            "description": "潮汐時間因子，格式為「hh:mm:ss」，預設為全部回傳"
          },
          {
            "name": "timeFrom",
            "required": False,
            "type": "string($date-time)",
            "description": "時間區段，篩選需要之時間區段，時間從「timeFrom」開始篩選，直到內容之最後時間，並可與參數「timeTo」合併使用，格式為「yyyy-MM-ddThh:mm:ss」，若使用參數「Date」或「hhmmss」，則參數「timeFrom」的篩選資料則會失效，預設為全部回傳"
          },
          {
            "name": "timeTo",
            "required": False,
            "type": "string($date-time)",
            "description": "時間區段，篩選需要之時間區段，時間從內容之最初時間開始篩選，直到「timeTo」，並可與參數「timeFrom」 合併使用，格式為「yyyy-MM-ddThh:mm:ss」，若使用「Date」或「hhmmss」，則參數「timeTo」的篩選資料則會失效，預設為全部回傳"
          }
        ]
      },
      {
        "path": "/v1/rest/datastore/F-A0085-002",
        "dataId": "F-A0085-002",
        "summary": "健康氣象冷傷害指數及警示全臺各鄉鎮五日預報",
        "description": "健康氣象相關預報資料-冷傷害指數及警示全臺各鄉鎮五日預報",
        "parameters": [
          {
            "name": "Authorization",
            "required": True,
            "type": "string",
            "description": "氣象開放資料平台會員授權碼"
          },
          {
            "name": "limit",
            "required": False,
            "type": "number($int)",
            "description": "限制最多回傳的資料, 預設為回傳全部筆數"
          },
          {
            "name": "offset",
            "required": False,
            "type": "number($int)",
            "description": "指定從第幾筆後開始回傳, 預設為第 0 筆開始回傳"
          },
          {
            "name": "format",
            "required": False,
            "type": "string",
            "description": "回傳資料格式, 預設為 json 格式Available values: JSON, XML--JSONXML"
          },
          {
            "name": "CountyName",
            "required": False,
            "type": "array[string]",
            "description": "各縣市名稱，預設為全部回傳Available values: 宜蘭縣, 花蓮縣, 臺東縣, 澎湖縣, 金門縣, 連江縣, 臺北市, 新北市, 桃園市, 臺中市, 臺南市, 高雄市, 基隆市, 新竹縣, 新竹市, 苗栗縣, 彰化縣, 南投縣, 雲林縣, 嘉義縣, 嘉義市, 屏東縣--宜蘭縣花蓮縣臺東縣澎湖縣金門縣連江縣臺北市新北市桃園市臺中市臺南市高雄市基隆市新竹縣新竹市苗栗縣彰化縣南投縣雲林縣嘉義縣嘉義市屏東縣"
          },
          {
            "name": "TownName",
            "required": False,
            "type": "array[string]",
            "description": "各縣市所對應鄉鎮名稱，請參考https://opendata.cwa.gov.tw/opendatadoc/Opendata_City.pdf，附錄 A『全臺縣市鄉鎮對照表』，預設為全部回傳"
          },
          {
            "name": "WeatherElements",
            "required": False,
            "type": "array[string]",
            "description": "天氣預報因子，預設為全部回傳Available values: ColdInjuryIndex, ColdInjuryWarning--ColdInjuryIndexColdInjuryWarning"
          },
          {
            "name": "StartTime",
            "required": False,
            "type": "array[string]",
            "description": "時間因子，預設全部回傳，格式為「yyyy-MM-ddThh:mm:ss」"
          },
          {
            "name": "timeFrom",
            "required": False,
            "type": "string($date)",
            "description": "時間區段，篩選需要之時間區段，時間從「timeFrom」 開始篩選，直到內容之最後時間，並可與參數 「timeTo」 合併使用，格式為「yyyy-MM-ddThh:mm:ss」若使用參數「StartTime」，則參數「timeFrom」的篩選資料則會失效，預設為全部回傳"
          },
          {
            "name": "timeTo",
            "required": False,
            "type": "string($date)",
            "description": "時間區段，篩選需要之時間區段，時間從內容之最初時間開始篩選，直到 timeTo，並可與參數 「timeFrom」 合併使用，格式為「yyyy-MM-ddThh:mm:ss」若使用「StartTime」，則參數「timeTo」的篩選資料則會失效，預設為全部回傳"
          },
          {
            "name": "sort",
            "required": False,
            "type": "array[string]",
            "description": "「StartTime」 為針對「StartTime」，預設不排序Available values: StartTime--StartTime"
          }
        ]
      },
      {
        "path": "/v1/rest/datastore/F-A0085-003",
        "dataId": "F-A0085-003",
        "summary": "健康氣象冷傷害指數及警示全臺各鄉鎮未來72小時逐3小時預報",
        "description": "健康氣象相關數值預報資料-熱傷害分級與綜合溫度熱指數",
        "parameters": [
          {
            "name": "Authorization",
            "required": True,
            "type": "string",
            "description": "氣象開放資料平台會員授權碼"
          },
          {
            "name": "limit",
            "required": False,
            "type": "number($int)",
            "description": "限制最多回傳的資料, 預設為回傳全部筆數"
          },
          {
            "name": "offset",
            "required": False,
            "type": "number($int)",
            "description": "指定從第幾筆後開始回傳, 預設為第 0 筆開始回傳"
          },
          {
            "name": "format",
            "required": False,
            "type": "string",
            "description": "回傳資料格式, 預設為 json 格式Available values: JSON, XML--JSONXML"
          },
          {
            "name": "CountyName",
            "required": False,
            "type": "array[string]",
            "description": "各縣市名稱，預設為全部回傳Available values: 宜蘭縣, 花蓮縣, 臺東縣, 澎湖縣, 金門縣, 連江縣, 臺北市, 新北市, 桃園市, 臺中市, 臺南市, 高雄市, 基隆市, 新竹縣, 新竹市, 苗栗縣, 彰化縣, 南投縣, 雲林縣, 嘉義縣, 嘉義市, 屏東縣--宜蘭縣花蓮縣臺東縣澎湖縣金門縣連江縣臺北市新北市桃園市臺中市臺南市高雄市基隆市新竹縣新竹市苗栗縣彰化縣南投縣雲林縣嘉義縣嘉義市屏東縣"
          },
          {
            "name": "TownName",
            "required": False,
            "type": "array[string]",
            "description": "各縣市所對應鄉鎮名稱，請參考https://opendata.cwa.gov.tw/opendatadoc/Opendata_City.pdf，附錄 A『全臺縣市鄉鎮對照表』，預設為全部回傳"
          },
          {
            "name": "WeatherElements",
            "required": False,
            "type": "array[string]",
            "description": "天氣預報因子，預設為全部回傳Available values: ColdInjuryIndex, ColdInjuryWarning--ColdInjuryIndexColdInjuryWarning"
          },
          {
            "name": "IssueTime",
            "required": False,
            "type": "array[string]",
            "description": "時間因子，預設全部回傳，格式為「yyyy-MM-ddThh:mm:ss」"
          },
          {
            "name": "timeFrom",
            "required": False,
            "type": "string($date)",
            "description": "時間區段，篩選需要之時間區段，時間從「timeFrom」 開始篩選，直到內容之最後時間，並可與參數 「timeTo」 合併使用，格式為「yyyy-MM-ddThh:mm:ss」若使用參數「dataTime」，則參數「timeFrom」的篩選資料則會失效，預設為全部回傳"
          },
          {
            "name": "timeTo",
            "required": False,
            "type": "string($date)",
            "description": "時間區段，篩選需要之時間區段，時間從內容之最初時間開始篩選，直到 timeTo，並可與參數 「timeFrom」 合併使用，格式為「yyyy-MM-ddThh:mm:ss」若使用「IssueTime」，則參數「timeTo」的篩選資料則會失效，預設為全部回傳"
          },
          {
            "name": "sort",
            "required": False,
            "type": "array[string]",
            "description": "「IssueTime」 為針對「IssueTime」，預設不排序Available values: IssueTime--IssueTime"
          }
        ]
      },
      {
        "path": "/v1/rest/datastore/F-A0085-004",
        "dataId": "F-A0085-004",
        "summary": "健康氣象溫差提醒指數及警示全臺各鄉鎮五日預報",
        "description": "健康氣象相關預報資料-健康氣象溫差提醒指數及警示全臺各鄉鎮五日預報",
        "parameters": [
          {
            "name": "Authorization",
            "required": True,
            "type": "string",
            "description": "氣象開放資料平台會員授權碼"
          },
          {
            "name": "limit",
            "required": False,
            "type": "number($int)",
            "description": "限制最多回傳的資料, 預設為回傳全部筆數"
          },
          {
            "name": "offset",
            "required": False,
            "type": "number($int)",
            "description": "指定從第幾筆後開始回傳, 預設為第 0 筆開始回傳"
          },
          {
            "name": "format",
            "required": False,
            "type": "string",
            "description": "回傳資料格式, 預設為 json 格式Available values: JSON, XML--JSONXML"
          },
          {
            "name": "CountyName",
            "required": False,
            "type": "array[string]",
            "description": "各縣市名稱，預設為全部回傳Available values: 宜蘭縣, 花蓮縣, 臺東縣, 澎湖縣, 金門縣, 連江縣, 臺北市, 新北市, 桃園市, 臺中市, 臺南市, 高雄市, 基隆市, 新竹縣, 新竹市, 苗栗縣, 彰化縣, 南投縣, 雲林縣, 嘉義縣, 嘉義市, 屏東縣--宜蘭縣花蓮縣臺東縣澎湖縣金門縣連江縣臺北市新北市桃園市臺中市臺南市高雄市基隆市新竹縣新竹市苗栗縣彰化縣南投縣雲林縣嘉義縣嘉義市屏東縣"
          },
          {
            "name": "TownName",
            "required": False,
            "type": "array[string]",
            "description": "各縣市所對應鄉鎮名稱，請參考https://opendata.cwa.gov.tw/opendatadoc/Opendata_City.pdf，附錄 A『全臺縣市鄉鎮對照表』，預設為全部回傳"
          },
          {
            "name": "WeatherElements",
            "required": False,
            "type": "array[string]",
            "description": "天氣預報因子，預設為全部回傳Available values: MaxTemperature, MinTemperature, TemperatureDifferenceWarning--MaxTemperatureMinTemperatureTemperatureDifferenceWarning"
          },
          {
            "name": "StartTime",
            "required": False,
            "type": "array[string]",
            "description": "時間因子，預設全部回傳，格式為「yyyy-MM-ddThh:mm:ss」"
          },
          {
            "name": "timeFrom",
            "required": False,
            "type": "string($date)",
            "description": "時間區段，篩選需要之時間區段，時間從「timeFrom」 開始篩選，直到內容之最後時間，並可與參數 「timeTo」 合併使用，格式為「yyyy-MM-ddThh:mm:ss」若使用參數「StartTime」，則參數「timeFrom」的篩選資料則會失效，預設為全部回傳"
          },
          {
            "name": "timeTo",
            "required": False,
            "type": "string($date)",
            "description": "時間區段，篩選需要之時間區段，時間從內容之最初時間開始篩選，直到 timeTo，並可與參數 「timeFrom」 合併使用，格式為「yyyy-MM-ddThh:mm:ss」若使用「StartTime」，則參數「timeTo」的篩選資料則會失效，預設為全部回傳"
          },
          {
            "name": "sort",
            "required": False,
            "type": "array[string]",
            "description": "「StartTime」 為針對「StartTime」做排序，預設不排序Available values: StartTime--StartTime"
          }
        ]
      },
      {
        "path": "/v1/rest/datastore/F-A0085-005",
        "dataId": "F-A0085-005",
        "summary": "健康氣象溫差提醒指數及警示全臺各鄉鎮未來72小時逐3小時預報",
        "description": "健康氣象相關數值預報資料-健康氣象溫差提醒指數及警示全臺各鄉鎮未來72小時逐3小時預報",
        "parameters": [
          {
            "name": "Authorization",
            "required": True,
            "type": "string",
            "description": "氣象開放資料平台會員授權碼"
          },
          {
            "name": "limit",
            "required": False,
            "type": "number($int)",
            "description": "限制最多回傳的資料, 預設為回傳全部筆數"
          },
          {
            "name": "offset",
            "required": False,
            "type": "number($int)",
            "description": "指定從第幾筆後開始回傳, 預設為第 0 筆開始回傳"
          },
          {
            "name": "format",
            "required": False,
            "type": "string",
            "description": "回傳資料格式, 預設為 json 格式Available values: JSON, XML--JSONXML"
          },
          {
            "name": "CountyName",
            "required": False,
            "type": "array[string]",
            "description": "各縣市名稱，預設為全部回傳Available values: 宜蘭縣, 花蓮縣, 臺東縣, 澎湖縣, 金門縣, 連江縣, 臺北市, 新北市, 桃園市, 臺中市, 臺南市, 高雄市, 基隆市, 新竹縣, 新竹市, 苗栗縣, 彰化縣, 南投縣, 雲林縣, 嘉義縣, 嘉義市, 屏東縣--宜蘭縣花蓮縣臺東縣澎湖縣金門縣連江縣臺北市新北市桃園市臺中市臺南市高雄市基隆市新竹縣新竹市苗栗縣彰化縣南投縣雲林縣嘉義縣嘉義市屏東縣"
          },
          {
            "name": "TownName",
            "required": False,
            "type": "array[string]",
            "description": "各縣市所對應鄉鎮名稱，請參考https://opendata.cwa.gov.tw/opendatadoc/Opendata_City.pdf，附錄 A『全臺縣市鄉鎮對照表』，預設為全部回傳"
          },
          {
            "name": "WeatherElements",
            "required": False,
            "type": "array[string]",
            "description": "天氣預報因子，預設為全部回傳Available values: TemperatureDifferenceIndex, TemperatureDifferenceWarning--TemperatureDifferenceIndexTemperatureDifferenceWarning"
          },
          {
            "name": "IssueTime",
            "required": False,
            "type": "array[string]",
            "description": "時間因子，預設全部回傳，格式為「yyyy-MM-ddThh:mm:ss」"
          },
          {
            "name": "timeFrom",
            "required": False,
            "type": "string($date)",
            "description": "時間區段，篩選需要之時間區段，時間從「timeFrom」 開始篩選，直到內容之最後時間，並可與參數 「timeTo」 合併使用，格式為「yyyy-MM-ddThh:mm:ss」若使用參數「dataTime」，則參數「timeFrom」的篩選資料則會失效，預設為全部回傳"
          },
          {
            "name": "timeTo",
            "required": False,
            "type": "string($date)",
            "description": "時間區段，篩選需要之時間區段，時間從內容之最初時間開始篩選，直到 timeTo，並可與參數 「timeFrom」 合併使用，格式為「yyyy-MM-ddThh:mm:ss」若使用「IssueTime」，則參數「timeTo」的篩選資料則會失效，預設為全部回傳"
          },
          {
            "name": "sort",
            "required": False,
            "type": "array[string]",
            "description": "「IssueTime」 為針對「IssueTime做排序」，預設不排序Available values: IssueTime--IssueTime"
          }
        ]
      }
    ]
  },
  "observation": {
    "cmd": "observation",
    "title": "觀測",
    "apis": [
      {
        "path": "/v1/rest/datastore/O-A0001-001",
        "dataId": "O-A0001-001",
        "summary": "自動氣象站-氣象觀測資料",
        "description": "自動氣象站資料-無人自動站氣象資料",
        "parameters": [
          {
            "name": "Authorization",
            "required": True,
            "type": "string",
            "description": "氣象開放資料平台會員授權碼"
          },
          {
            "name": "limit",
            "required": False,
            "type": "number($int)",
            "description": "限制最多回傳的資料，預設為回傳全部筆數"
          },
          {
            "name": "offset",
            "required": False,
            "type": "number($int)",
            "description": "指定從第幾筆後開始回傳，預設為第 0 筆開始回傳"
          },
          {
            "name": "format",
            "required": False,
            "type": "string",
            "description": "回傳資料格式，預設為 json 格式Available values: JSON, XML--JSONXML"
          },
          {
            "name": "StationId",
            "required": False,
            "type": "array[string]",
            "description": "測站站號，請參考https://e-service.cwa.gov.tw/wdps/obs/state.htm，可輸入多個站號，大小寫必須完全符合，預設為全部回傳"
          },
          {
            "name": "StationName",
            "required": False,
            "type": "array[string]",
            "description": "測站站名，請參考https://e-service.cwa.gov.tw/wdps/obs/state.htm，可輸入多個站名，預設為全部回傳，若使用「StationId」，則參數「StationName」的篩選資料則會失效，只會回傳StationId符合的資料"
          },
          {
            "name": "WeatherElement",
            "required": False,
            "type": "array[string]",
            "description": "氣象因子，預設為全部回傳Available values: Weather, Now, WindDirection, WindSpeed, AirTemperature, RelativeHumidity, AirPressure, GustInfo, DailyHigh, DailyLow--WeatherNowWindDirectionWindSpeedAirTemperatureRelativeHumidityAirPressureGustInfoDailyHighDailyLow"
          },
          {
            "name": "GeoInfo",
            "required": False,
            "type": "array[string]",
            "description": "參數，預設為全部回傳Available values: Coordinates, StationAltitude, CountyName, TownName, CountyCode, TownCode--CoordinatesStationAltitudeCountyNameTownNameCountyCodeTownCode"
          }
        ]
      },
      {
        "path": "/v1/rest/datastore/O-A0002-001",
        "dataId": "O-A0002-001",
        "summary": "自動雨量站-雨量觀測資料",
        "description": "自動雨量站資料-無人自動站雨量資料",
        "parameters": [
          {
            "name": "Authorization",
            "required": True,
            "type": "string",
            "description": "氣象開放資料平台會員授權碼"
          },
          {
            "name": "limit",
            "required": False,
            "type": "number($int)",
            "description": "限制最多回傳的資料，預設為回傳全部筆數"
          },
          {
            "name": "offset",
            "required": False,
            "type": "number($int)",
            "description": "指定從第幾筆後開始回傳，預設為第 0 筆開始回傳"
          },
          {
            "name": "format",
            "required": False,
            "type": "string",
            "description": "回傳資料格式，預設為 json 格式Available values: JSON, XML--JSONXML"
          },
          {
            "name": "StationId",
            "required": False,
            "type": "array[string]",
            "description": "測站站號，請參考https://e-service.cwa.gov.tw/wdps/obs/state.htm，可輸入多個站號，大小寫必須完全符合，預設為全部回傳"
          },
          {
            "name": "StationName",
            "required": False,
            "type": "array[string]",
            "description": "測站站名，請參考https://e-service.cwa.gov.tw/wdps/obs/state.htm，可輸入多個站名，預設為全部回傳，若使用「StationId」，則參數「StationName」的篩選資料則會失效，只會回傳StationId符合的資料"
          },
          {
            "name": "RainfallElement",
            "required": False,
            "type": "array[string]",
            "description": "氣象因子，預設為全部回傳Available values: Now, Past10Min, Past1hr, Past3hr, Past6hr, Past12hr, Past24hr, Past2days, Past3days--NowPast10MinPast1hrPast3hrPast6hrPast12hrPast24hrPast2daysPast3days"
          },
          {
            "name": "GeoInfo",
            "required": False,
            "type": "array[string]",
            "description": "參數，預設為全部回傳Available values: Coordinates, StationAltitude, CountyName, TownName, CountyCode, TownCode--CoordinatesStationAltitudeCountyNameTownNameCountyCodeTownCode"
          }
        ]
      },
      {
        "path": "/v1/rest/datastore/O-A0003-001",
        "dataId": "O-A0003-001",
        "summary": "現在天氣觀測報告-現在天氣觀測報告",
        "description": "現在天氣觀測報告-有人氣象站資料",
        "parameters": [
          {
            "name": "Authorization",
            "required": True,
            "type": "string",
            "description": "氣象開放資料平台會員授權碼"
          },
          {
            "name": "limit",
            "required": False,
            "type": "number($int)",
            "description": "限制最多回傳的資料，預設為回傳全部筆數"
          },
          {
            "name": "offset",
            "required": False,
            "type": "number($int)",
            "description": "指定從第幾筆後開始回傳，預設為第 0 筆開始回傳"
          },
          {
            "name": "format",
            "required": False,
            "type": "string",
            "description": "回傳資料格式，預設為 json 格式Available values: JSON, XML--JSONXML"
          },
          {
            "name": "StationId",
            "required": False,
            "type": "array[string]",
            "description": "測站站號，請參考https://e-service.cwa.gov.tw/wdps/obs/state.htm，可輸入多個站號，大小寫必須完全符合，預設為全部回傳"
          },
          {
            "name": "StationName",
            "required": False,
            "type": "array[string]",
            "description": "測站站名，請參考https://e-service.cwa.gov.tw/wdps/obs/state.htm，可輸入多個站名，預設為全部回傳，若使用「StationId」，則參數「StationName」的篩選資料則會失效，只會回傳StationId符合的資料"
          },
          {
            "name": "WeatherElement",
            "required": False,
            "type": "array[string]",
            "description": "氣象因子，預設為全部回傳Available values: Weather, VisibilityDescription, SunshineDuration, Now, WindDirection, WindSpeed, AirTemperature, RelativeHumidity, AirPressure, UVIndex, Max10MinAverage, GustInfo, DailyHigh, DailyLow--WeatherVisibilityDescriptionSunshineDurationNowWindDirectionWindSpeedAirTemperatureRelativeHumidityAirPressureUVIndexMax10MinAverageGustInfoDailyHighDailyLow"
          },
          {
            "name": "GeoInfo",
            "required": False,
            "type": "array[string]",
            "description": "參數，預設為全部回傳Available values: Coordinates, StationAltitude, CountyName, TownName, CountyCode, TownCode--CoordinatesStationAltitudeCountyNameTownNameCountyCodeTownCode"
          }
        ]
      },
      {
        "path": "/v1/rest/datastore/O-A0004-001",
        "dataId": "O-A0004-001",
        "summary": "酸雨 pH 值-每日酸雨 pH 值",
        "description": "氣象站每日酸雨pH值-每月各站的資料",
        "parameters": [
          {
            "name": "Authorization",
            "required": True,
            "type": "string",
            "description": "氣象開放資料平台會員授權碼"
          },
          {
            "name": "limit",
            "required": False,
            "type": "number($int)",
            "description": "限制最多回傳的資料，預設為回傳全部筆數"
          },
          {
            "name": "offset",
            "required": False,
            "type": "number($int)",
            "description": "指定從第幾筆後開始回傳，預設為第 0 筆開始回傳"
          },
          {
            "name": "format",
            "required": False,
            "type": "string",
            "description": "回傳資料格式，預設為 json 格式Available values: JSON, XML--JSONXML"
          },
          {
            "name": "locationName",
            "required": False,
            "type": "array[string]",
            "description": "測站站名，請參考https://e-service.cwa.gov.tw/wdps/obs/state.htm，預設為全部回傳"
          },
          {
            "name": "elementName",
            "required": False,
            "type": "array[string]",
            "description": "月份因子若名稱為「中央氣象署各氣象站 2015 年 9月份雨水酸鹼度值」，則使用「2015-09」 查詢，格式為「yyyy-MM」，預設為全部回傳"
          },
          {
            "name": "parameterName",
            "required": False,
            "type": "array[string]",
            "description": "參數，預設為全部回傳Available values: mean, max, min, sap--meanmaxminsap"
          },
          {
            "name": "sort",
            "required": False,
            "type": "array[string]",
            "description": "「time」 為針對月份因子做升冪排序，「dataTime」 為針對時間因子做升冪排序，預設不排序Available values: time, dataTime--timedataTime"
          },
          {
            "name": "dataTime",
            "required": False,
            "type": "array[string]",
            "description": "時間因子，格式為「yyyy-MM-dd」"
          },
          {
            "name": "timeFrom",
            "required": False,
            "type": "string($date-time)",
            "description": "時間區段，篩選需要之時間區段，時間從「timeFrom」開始篩選，直到內容之最後時間，並可與參數「timeTo」 合併使用，格式為「yyyy-MM-ddThh:mm:ss」，若使用參數「dataTime」，則參數「timeFrom」的篩選資料則會失效，預設為全部回傳"
          },
          {
            "name": "timeTo",
            "required": False,
            "type": "string($date-time)",
            "description": "時間區段，篩選需要之時間區段，時間從內容之最初時間開始篩選，直到「timeTo」，並可與參數「timeFrom」 合併使用，格式為「yyyy-MM-ddThh:mm:ss」，若使用「dataTime」，則參數「timeTo」的篩選資料則會失效，預設為全部回傳"
          }
        ]
      },
      {
        "path": "/v1/rest/datastore/O-A0005-001",
        "dataId": "O-A0005-001",
        "summary": "紫外線指數-每日紫外線指數最大值",
        "description": "氣象站每日紫外線指數最大值-每天下午2時左右會提供各站紫外線的當日最大值",
        "parameters": [
          {
            "name": "Authorization",
            "required": True,
            "type": "string",
            "description": "氣象開放資料平台會員授權碼"
          },
          {
            "name": "limit",
            "required": False,
            "type": "number($int)",
            "description": "限制最多回傳的資料，預設為回傳全部筆數"
          },
          {
            "name": "offset",
            "required": False,
            "type": "number($int)",
            "description": "指定從第幾筆後開始回傳，預設為第 0 筆開始回傳"
          },
          {
            "name": "format",
            "required": False,
            "type": "string",
            "description": "回傳資料格式，預設為 json 格式Available values: JSON, XML--JSONXML"
          },
          {
            "name": "StationID",
            "required": False,
            "type": "array[string]",
            "description": "測站站號，請參考https://e-service.cwa.gov.tw/wdps/obs/state.htm，預設為全部回傳"
          }
        ]
      },
      {
        "path": "/v1/rest/datastore/O-A0006-002",
        "dataId": "O-A0006-002",
        "summary": "臭氧總量觀測資料-台北站",
        "description": "臭氧總量觀測資料-臭氧總量觀測資料(台北)",
        "parameters": [
          {
            "name": "Authorization",
            "required": True,
            "type": "string",
            "description": "氣象開放資料平台會員授權碼"
          },
          {
            "name": "limit",
            "required": False,
            "type": "number($int)",
            "description": "限制最多回傳的資料，預設為回傳全部筆數"
          },
          {
            "name": "offset",
            "required": False,
            "type": "number($int)",
            "description": "指定從第幾筆後開始回傳，預設為第 0 筆開始回傳"
          },
          {
            "name": "format",
            "required": False,
            "type": "string",
            "description": "回傳資料格式，預設為 json 格式Available values: JSON, XML--JSONXML"
          },
          {
            "name": "elementName",
            "required": False,
            "type": "array[string]",
            "description": "臭氧量統計因子，預設為全部回傳Available values: 累年臭氧全量累年平均值, 累年臭氧全量累年月平均值最低, 累年臭氧全量月平均值, 累年臭氧全量累年月平均值, 累年臭氧全量累年月平均值最高--累年臭氧全量累年平均值累年臭氧全量累年月平均值最低累年臭氧全量月平均值累年臭氧全量累年月平均值累年臭氧全量累年月平均值最高"
          },
          {
            "name": "dataTime",
            "required": False,
            "type": "array[string]",
            "description": "時間因子，格式有 「yyyy」，「MM」，「yyyyy-MM」，預設為全部回傳"
          },
          {
            "name": "sort",
            "required": False,
            "type": "string",
            "description": "進行時間升冪排序，預設不排序Available values: dataTime--dataTime"
          }
        ]
      },
      {
        "path": "/v1/rest/datastore/O-B0075-001",
        "dataId": "O-B0075-001",
        "summary": "海象監測資料-48小時浮標站與潮位站海況監測資料",
        "description": "海象監測資料-48小時浮標站與潮位站海況監測資料",
        "parameters": [
          {
            "name": "Authorization",
            "required": True,
            "type": "string",
            "description": "氣象開放資料平台會員授權碼"
          },
          {
            "name": "limit",
            "required": False,
            "type": "number($int)",
            "description": "限制最多回傳的資料，預設為回傳全部筆數"
          },
          {
            "name": "offset",
            "required": False,
            "type": "number($int)",
            "description": "指定從第幾筆後開始回傳，預設為第 0 筆開始回傳"
          },
          {
            "name": "format",
            "required": False,
            "type": "string",
            "description": "回傳資料格式，預設為 json 格式Available values: JSON, XML--JSONXML"
          },
          {
            "name": "StationID",
            "required": False,
            "type": "array[string]",
            "description": "測站代碼，請參考https://opendata.cwa.gov.tw/dataset/observation/O-B0076-001"
          },
          {
            "name": "WeatherElement",
            "required": False,
            "type": "array[string]",
            "description": "氣象因子，預設為全部回傳Available values: TideHeight, TideLevel, WaveHeight, WaveDirection, WaveDirectionDescription, WavePeriod, SeaTemperature, Temperature, StationPressure, PrimaryAnemometer, SeaCurrents--TideHeightTideLevelWaveHeightWaveDirectionWaveDirectionDescriptionWavePeriodSeaTemperatureTemperatureStationPressurePrimaryAnemometerSeaCurrents"
          },
          {
            "name": "sort",
            "required": False,
            "type": "string",
            "description": "針對 「StationID」或「DataTime」做升冪排序，預設不排序Available values: StationID, DataTime--StationIDDataTime"
          },
          {
            "name": "DataTime",
            "required": False,
            "type": "array[string]",
            "description": "時間因子，格式為「yyyy-MM-ddThh:mm:ss」，預設全部回傳"
          },
          {
            "name": "timeFrom",
            "required": False,
            "type": "string($date-time)",
            "description": "時間區段，篩選需要之時間區段，時間從「timeFrom」 開始篩選，直到內容之最後時間，並可與參數「timeTo」 合併使用，格式為「yyyy-MM-ddThh:mm:ss」。 若使用參數「DataTime」，則參數「timeFrom」的篩選資料則會失效。預設全部回傳"
          },
          {
            "name": "timeTo",
            "required": False,
            "type": "string($date-time)",
            "description": "時間區段，篩選需要之時間區段，時間從內容之最初時間開始篩選，直到「timeTo」，並可與參數「timeFrom」 合併使用，格式為「yyyy-MM-ddThh:mm:ss」。 若使用「DataTime」，則參數「timeTo」的篩選資料則會失效。預設全部回傳"
          }
        ]
      },
      {
        "path": "/v1/rest/datastore/O-B0075-002",
        "dataId": "O-B0075-002",
        "summary": "海象監測資料-30天浮標站與潮位站海況監測資料",
        "description": "海象監測資料-30天浮標站與潮位站海況監測資料",
        "parameters": [
          {
            "name": "Authorization",
            "required": True,
            "type": "string",
            "description": "氣象開放資料平台會員授權碼"
          },
          {
            "name": "limit",
            "required": False,
            "type": "number($int)",
            "description": "限制最多回傳的資料，預設為回傳全部筆數"
          },
          {
            "name": "offset",
            "required": False,
            "type": "number($int)",
            "description": "指定從第幾筆後開始回傳，預設為第 0 筆開始回傳"
          },
          {
            "name": "format",
            "required": False,
            "type": "string",
            "description": "回傳資料格式，預設為 json 格式Available values: JSON, XML--JSONXML"
          },
          {
            "name": "StationID",
            "required": False,
            "type": "array[string]",
            "description": "測站代碼，請參考https://opendata.cwa.gov.tw/dataset/observation/O-B0076-001"
          },
          {
            "name": "WeatherElement",
            "required": False,
            "type": "array[string]",
            "description": "氣象因子，預設為全部回傳Available values: TideHeight, TideLevel, WaveHeight, WaveDirection, WaveDirectionDescription, WavePeriod, SeaTemperature, Temperature, StationPressure, PrimaryAnemometer, SeaCurrents--TideHeightTideLevelWaveHeightWaveDirectionWaveDirectionDescriptionWavePeriodSeaTemperatureTemperatureStationPressurePrimaryAnemometerSeaCurrents"
          },
          {
            "name": "sort",
            "required": False,
            "type": "string",
            "description": "針對 「StationID」或「DataTime」做升冪排序，預設不排序Available values: StationID, DataTime--StationIDDataTime"
          },
          {
            "name": "DataTime",
            "required": False,
            "type": "array[string]",
            "description": "時間因子，格式為「yyyy-MM-ddThh:mm:ss」，最多回傳24個小時的資料。預設回傳最早24個小時的資料。"
          },
          {
            "name": "timeFrom",
            "required": False,
            "type": "string($date-time)",
            "description": "時間區段，篩選需要之時間區段，格式為「yyyy-MM-ddThh:mm:ss」時間從「timeFrom」開始篩選，直到「timeFrom」之後24小時的資料並可與參數 「timeTo」 合併使用，時間從「timeFrom」開始篩選，直到「timeTo」，可回傳最多24小時長度的資料在合併使用參數「timeTo」和參數「timeFrom」的時候，若是 「timeTo」的時間超過「timeFrom」之後24小時，則僅會回傳「timeFrom」開始後24小時之間的資料若使用參數「DataTime」，則參數「timeFrom」的篩選資料則會失效若是參數「timeFrom」和參數「timeTo」都沒有設定，預設會回傳內容中最初24小時的資料"
          },
          {
            "name": "timeTo",
            "required": False,
            "type": "string($date-time)",
            "description": "時間區段，篩選需要之時間區段，格式為「yyyy-MM-ddThh:mm:ss」時間從「timeTo」之前24小時開始篩選，直到「timeTo」並可與參數 「timeFrom」 合併使用，時間從「timeFrom」開始篩選，直到「timeTo」，可回傳最多24小時長度的資料在合併使用參數「timeTo」和參數「timeFrom」的時候，若是 「timeTo」的時間超過「timeFrom」之後24小時，則僅會回傳「timeFrom」開始後24小時之間的資料若使用參數「DataTime」，則參數「timeTo」的篩選資料則會失效若是參數「timeFrom」和參數「timeTo」都沒有設定，預設會回傳內容中最初24小時的資料"
          }
        ]
      }
    ]
  },
  "earthquake": {
    "cmd": "earthquake",
    "title": "地震海嘯",
    "apis": [
      {
        "path": "/v1/rest/datastore/E-A0014-001",
        "dataId": "E-A0014-001",
        "summary": "海嘯資訊資料-海嘯資訊資料",
        "description": "海嘯資訊資料",
        "parameters": [
          {
            "name": "Authorization",
            "required": True,
            "type": "string",
            "description": "氣象開放資料平台會員授權碼"
          },
          {
            "name": "limit",
            "required": False,
            "type": "number($int)",
            "description": "限制最多回傳的資料，預設為回傳全部筆數"
          },
          {
            "name": "offset",
            "required": False,
            "type": "number($int)",
            "description": "指定從第幾筆後開始回傳，預設為第 0 筆開始回傳"
          },
          {
            "name": "format",
            "required": False,
            "type": "string",
            "description": "回傳資料格式，預設為 json 格式Available values: JSON, XML--JSONXML"
          },
          {
            "name": "AreaName",
            "required": False,
            "type": "array[string]",
            "description": "區域名稱 ，預設為全部回傳"
          },
          {
            "name": "StationName",
            "required": False,
            "type": "array[string]",
            "description": "測站名稱，預設為全部回傳"
          },
          {
            "name": "sort",
            "required": False,
            "type": "array[string]",
            "description": "「OriginTime」為針對「OriginTime」與「ReportNo」做升冪排序，預設「OriginTime」與「ReportNo」為降冪排序Available values: OriginTime--OriginTime"
          },
          {
            "name": "OriginTime",
            "required": False,
            "type": "array[string]",
            "description": "時間因子，格式為「yyyy-MM-ddThh:mm:ss」，預設為全部回傳"
          },
          {
            "name": "timeFrom",
            "required": False,
            "type": "string($date-time)",
            "description": "時間區段，篩選需要之時間區段，時間從「timeFrom」開始篩選，直到內容之最後時間，並可與參數 「timeTo」 合併使用，格式為「yyyy-MM-ddThh:mm:ss」，若使用參數「dataTime」，則參數「timeFrom」的篩選資料則會失效 ，預設為全部回傳"
          },
          {
            "name": "timeTo",
            "required": False,
            "type": "string($date-time)",
            "description": "時間區段，篩選需要之時間區段，時間從內容之最初時間開始篩選，直到「timeTo」，並可與參數 timeFrom」 合併使用，格式為「yyyy-MM-ddThh:mm:ss」，若使用「dataTime」，則參數「timeTo」的篩選資料則會失效，預設為全部回傳"
          }
        ]
      },
      {
        "path": "/v1/rest/datastore/E-A0015-001",
        "dataId": "E-A0015-001",
        "summary": "顯著有感地震報告資料-顯著有感地震報告",
        "description": "顯著有感地震報告",
        "parameters": [
          {
            "name": "Authorization",
            "required": True,
            "type": "string",
            "description": "氣象開放資料平台會員授權碼"
          },
          {
            "name": "limit",
            "required": False,
            "type": "number($int)",
            "description": "限制最多回傳的資料，預設為回傳全部筆數"
          },
          {
            "name": "offset",
            "required": False,
            "type": "number($int)",
            "description": "指定從第幾筆後開始回傳，預設為第 0 筆開始回傳"
          },
          {
            "name": "format",
            "required": False,
            "type": "string",
            "description": "回傳資料格式，預設為 json 格式Available values: JSON, XML--JSONXML"
          },
          {
            "name": "AreaName",
            "required": False,
            "type": "array[string]",
            "description": "臺灣各縣市Available values: 宜蘭縣, 花蓮縣, 臺東縣, 澎湖縣, 金門縣, 連江縣, 臺北市, 新北市, 桃園市, 臺中市, 臺南市, 高雄市, 基隆市, 新竹縣, 新竹市, 苗栗縣, 彰化縣, 南投縣, 雲林縣, 嘉義縣, 嘉義市, 屏東縣--宜蘭縣花蓮縣臺東縣澎湖縣金門縣連江縣臺北市新北市桃園市臺中市臺南市高雄市基隆市新竹縣新竹市苗栗縣彰化縣南投縣雲林縣嘉義縣嘉義市屏東縣"
          },
          {
            "name": "StationName",
            "required": False,
            "type": "array[string]",
            "description": "測站名稱，預設為全部回傳"
          },
          {
            "name": "sort",
            "required": False,
            "type": "string[string]",
            "description": "設為「OriginTime」為針對時間因子做升冪排序，預設為降冪排序Available values: OriginTime"
          },
          {
            "name": "OriginTime",
            "required": False,
            "type": "array[string]",
            "description": "時間因子，格式為「yyyy-MM-ddThh:mm:ss」，預設為全部回傳"
          },
          {
            "name": "timeFrom",
            "required": False,
            "type": "string($date-time)",
            "description": "時間區段，篩選需要之時間區段，時間從「timeFrom」開始篩選，直到內容之最後時間，並可與參數 「timeTo」 合併使用，格式為「yyyy-MM-ddThh:mm:ss」，若使用參數「dataTime」，則參數「timeFrom」的篩選資料則會失效 ，預設為全部回傳"
          },
          {
            "name": "timeTo",
            "required": False,
            "type": "string($date-time)",
            "description": "時間區段，篩選需要之時間區段，時間從內容之最初時間開始篩選，直到「timeTo」，並可與參數 timeFrom」 合併使用，格式為「yyyy-MM-ddThh:mm:ss」，若使用「dataTime」，則參數「timeTo」的篩選資料則會失效，預設為全部回傳"
          }
        ]
      },
      {
        "path": "/v1/rest/datastore/E-A0015-002",
        "dataId": "E-A0015-002",
        "summary": "顯著有感地震報告資料-顯著有感地震報告(英文)",
        "description": "提供顯著有感地震報告資料-英文版地震報告",
        "parameters": [
          {
            "name": "Authorization",
            "required": True,
            "type": "string",
            "description": "氣象開放資料平台會員授權碼"
          },
          {
            "name": "limit",
            "required": False,
            "type": "number($int)",
            "description": "限制最多回傳的資料，預設為回傳全部筆數"
          },
          {
            "name": "offset",
            "required": False,
            "type": "number($int)",
            "description": "指定從第幾筆後開始回傳，預設為第 0 筆開始回傳"
          },
          {
            "name": "format",
            "required": False,
            "type": "string",
            "description": "回傳資料格式，預設為 json 格式Available values: JSON, XML--JSONXML"
          },
          {
            "name": "AreaName",
            "required": False,
            "type": "array[string]",
            "description": "臺灣各縣市Available values: Yilan County, Hualien County, Taitung County, Penghu County, Kinmen County, Lienchiang County, Taipei City, New Taipei City, Taoyuan City, Taichung City, Tainan City, Kaohsiung City, Keelung City, Hsinchu County, Hsinchu City, Miaoli County, Changhua County, Nantou County, Yunlin County, Chiayi County, Chiayi City, Pingtung County--Yilan CountyHualien CountyTaitung CountyPenghu CountyKinmen CountyLienchiang CountyTaipei CityNew Taipei CityTaoyuan CityTaichung CityTainan CityKaohsiung CityKeelung CityHsinchu CountyHsinchu CityMiaoli CountyChanghua CountyNantou CountyYunlin CountyChiayi CountyChiayi CityPingtung County"
          },
          {
            "name": "StationName",
            "required": False,
            "type": "array[string]",
            "description": "測站名稱，預設為全部回傳"
          },
          {
            "name": "sort",
            "required": False,
            "type": "string[string]",
            "description": "設為「OriginTime」為針對時間因子做升冪排序，預設為降冪排序Available values: OriginTime"
          },
          {
            "name": "OriginTime",
            "required": False,
            "type": "array[string]",
            "description": "時間因子，格式為「yyyy-MM-ddThh:mm:ss」，預設為全部回傳"
          },
          {
            "name": "timeFrom",
            "required": False,
            "type": "string($date-time)",
            "description": "時間區段，篩選需要之時間區段，時間從「timeFrom」開始篩選，直到內容之最後時間，並可與參數 「timeTo」 合併使用，格式為「yyyy-MM-ddThh:mm:ss」，若使用參數「dataTime」，則參數「timeFrom」的篩選資料則會失效 ，預設為全部回傳"
          },
          {
            "name": "timeTo",
            "required": False,
            "type": "string($date-time)",
            "description": "時間區段，篩選需要之時間區段，時間從內容之最初時間開始篩選，直到「timeTo」，並可與參數 timeFrom」 合併使用，格式為「yyyy-MM-ddThh:mm:ss」，若使用「dataTime」，則參數「timeTo」的篩選資料則會失效，預設為全部回傳"
          }
        ]
      },
      {
        "path": "/v1/rest/datastore/E-A0016-001",
        "dataId": "E-A0016-001",
        "summary": "小區域有感地震報告資料-小區域有感地震報告",
        "description": "小區域有感地震報告",
        "parameters": [
          {
            "name": "Authorization",
            "required": True,
            "type": "string",
            "description": "氣象開放資料平台會員授權碼"
          },
          {
            "name": "limit",
            "required": False,
            "type": "number($int)",
            "description": "限制最多回傳的資料，預設為回傳全部筆數"
          },
          {
            "name": "offset",
            "required": False,
            "type": "number($int)",
            "description": "指定從第幾筆後開始回傳，預設為第 0 筆開始回傳"
          },
          {
            "name": "format",
            "required": False,
            "type": "string",
            "description": "回傳資料格式，預設為 json 格式Available values: JSON, XML--JSONXML"
          },
          {
            "name": "AreaName",
            "required": False,
            "type": "array[string]",
            "description": "臺灣各縣市Available values: 宜蘭縣, 花蓮縣, 臺東縣, 澎湖縣, 金門縣, 連江縣, 臺北市, 新北市, 桃園市, 臺中市, 臺南市, 高雄市, 基隆市, 新竹縣, 新竹市, 苗栗縣, 彰化縣, 南投縣, 雲林縣, 嘉義縣, 嘉義市, 屏東縣--宜蘭縣花蓮縣臺東縣澎湖縣金門縣連江縣臺北市新北市桃園市臺中市臺南市高雄市基隆市新竹縣新竹市苗栗縣彰化縣南投縣雲林縣嘉義縣嘉義市屏東縣"
          },
          {
            "name": "StationName",
            "required": False,
            "type": "array[string]",
            "description": "測站名稱，預設為全部回傳"
          },
          {
            "name": "sort",
            "required": False,
            "type": "string[string]",
            "description": "設為「OriginTime」為針對時間因子做升冪排序，預設為降冪排序Available values: OriginTime"
          },
          {
            "name": "OriginTime",
            "required": False,
            "type": "array[string]",
            "description": "時間因子，格式為「yyyy-MM-ddThh:mm:ss」，預設為全部回傳"
          },
          {
            "name": "timeFrom",
            "required": False,
            "type": "string($date-time)",
            "description": "時間區段，篩選需要之時間區段，時間從「timeFrom」開始篩選，直到內容之最後時間，並可與參數 「timeTo」 合併使用，格式為「yyyy-MM-ddThh:mm:ss」，若使用參數「dataTime」，則參數「timeFrom」的篩選資料則會失效 ，預設為全部回傳"
          },
          {
            "name": "timeTo",
            "required": False,
            "type": "string($date-time)",
            "description": "時間區段，篩選需要之時間區段，時間從內容之最初時間開始篩選，直到「timeTo」，並可與參數 timeFrom」 合併使用，格式為「yyyy-MM-ddThh:mm:ss」，若使用「dataTime」，則參數「timeTo」的篩選資料則會失效，預設為全部回傳"
          }
        ]
      },
      {
        "path": "/v1/rest/datastore/E-A0016-002",
        "dataId": "E-A0016-002",
        "summary": "小區域有感地震報告資料-小區域有感地震報告(英文)",
        "description": "提供小區域有感地震報告資料-英文版地震報告",
        "parameters": [
          {
            "name": "Authorization",
            "required": True,
            "type": "string",
            "description": "氣象開放資料平台會員授權碼"
          },
          {
            "name": "limit",
            "required": False,
            "type": "number($int)",
            "description": "限制最多回傳的資料，預設為回傳全部筆數"
          },
          {
            "name": "offset",
            "required": False,
            "type": "number($int)",
            "description": "指定從第幾筆後開始回傳，預設為第 0 筆開始回傳"
          },
          {
            "name": "format",
            "required": False,
            "type": "string",
            "description": "回傳資料格式，預設為 json 格式Available values: JSON, XML--JSONXML"
          },
          {
            "name": "AreaName",
            "required": False,
            "type": "array[string]",
            "description": "臺灣各縣市Available values: Yilan County, Hualien County, Taitung County, Penghu County, Kinmen County, Lienchiang County, Taipei City, New Taipei City, Taoyuan City, Taichung City, Tainan City, Kaohsiung City, Keelung City, Hsinchu County, Hsinchu City, Miaoli County, Changhua County, Nantou County, Yunlin County, Chiayi County, Chiayi City, Pingtung County--Yilan CountyHualien CountyTaitung CountyPenghu CountyKinmen CountyLienchiang CountyTaipei CityNew Taipei CityTaoyuan CityTaichung CityTainan CityKaohsiung CityKeelung CityHsinchu CountyHsinchu CityMiaoli CountyChanghua CountyNantou CountyYunlin CountyChiayi CountyChiayi CityPingtung County"
          },
          {
            "name": "StationName",
            "required": False,
            "type": "array[string]",
            "description": "測站名稱，預設為全部回傳"
          },
          {
            "name": "sort",
            "required": False,
            "type": "string[string]",
            "description": "設為「OriginTime」為針對時間因子做升冪排序，預設為降冪排序Available values: OriginTime"
          },
          {
            "name": "OriginTime",
            "required": False,
            "type": "array[string]",
            "description": "時間因子，格式為「yyyy-MM-ddThh:mm:ss」，預設為全部回傳"
          },
          {
            "name": "timeFrom",
            "required": False,
            "type": "string($date-time)",
            "description": "時間區段，篩選需要之時間區段，時間從「timeFrom」開始篩選，直到內容之最後時間，並可與參數 「timeTo」 合併使用，格式為「yyyy-MM-ddThh:mm:ss」，若使用參數「dataTime」，則參數「timeFrom」的篩選資料則會失效 ，預設為全部回傳"
          },
          {
            "name": "timeTo",
            "required": False,
            "type": "string($date-time)",
            "description": "時間區段，篩選需要之時間區段，時間從內容之最初時間開始篩選，直到「timeTo」，並可與參數 timeFrom」 合併使用，格式為「yyyy-MM-ddThh:mm:ss」，若使用「dataTime」，則參數「timeTo」的篩選資料則會失效，預設為全部回傳"
          }
        ]
      }
    ]
  },
  "climate": {
    "cmd": "climate",
    "title": "氣候",
    "apis": [
      {
        "path": "/v1/rest/datastore/C-B0025-001",
        "dataId": "C-B0025-001",
        "summary": "每日雨量-地面測站每日雨量資料",
        "description": "地面測站每日雨量資料-每日雨量",
        "parameters": [
          {
            "name": "Authorization",
            "required": True,
            "type": "string",
            "description": "氣象開放資料平台會員授權碼"
          },
          {
            "name": "limit",
            "required": False,
            "type": "number($int)",
            "description": "限制最多回傳的資料，預設為回傳全部筆數"
          },
          {
            "name": "offset",
            "required": False,
            "type": "number($int)",
            "description": "指定從第幾筆後開始回傳，預設為第 0 筆開始回傳"
          },
          {
            "name": "format",
            "required": False,
            "type": "string",
            "description": "回傳資料格式，預設為 json 格式Available values: JSON, XML--JSONXML"
          },
          {
            "name": "StationID",
            "required": False,
            "type": "array[string]",
            "description": "測站站號，請參考https://e-service.cwa.gov.tw/wdps/obs/state.htm，預設為全部回傳"
          },
          {
            "name": "sort",
            "required": False,
            "type": "array[string]",
            "description": "「time」 為針對月份因子做升冪排序，「dataTime」為針對時間因子做升冪排序，預設不排序Available values: dataTime--dataTime"
          },
          {
            "name": "Date",
            "required": False,
            "type": "array[string]",
            "description": "時間因子，格式為 「yyyy-MM-dd」，預設為全部回傳"
          },
          {
            "name": "timeFrom",
            "required": False,
            "type": "string($date-time)",
            "description": "時間區段，篩選需要之時間區段，時間從「timeFrom」開始篩選，直到內容之最後時間，並可與參數 「timeTo」 合併使用，格式為「yyyy-MM-dd」，若使用參數「Date」，則參數「timeFrom」的篩選資料則會失效 ，預設為全部回傳"
          },
          {
            "name": "timeTo",
            "required": False,
            "type": "string($date-time)",
            "description": "時間區段，篩選需要之時間區段，時間從內容之最初時間開始篩選，直到「timeTo」，並可與參數 timeFrom」 合併使用，格式為「yyyy-MM-dd」，若使用「Date」，則參數「timeTo」的篩選資料則會失效，預設為全部回傳"
          },
          {
            "name": "statistics",
            "required": False,
            "type": "boolean",
            "description": "是否選取每月雨量統計值，若選取的話則只回傳統計值，並且參數「Date」，參數「timeTo」，參數「timeFrom」失效。 預設為False--TrueFalse"
          }
        ]
      },
      {
        "path": "/v1/rest/datastore/C-B0027-001",
        "dataId": "C-B0027-001",
        "summary": "月平均-地面測站資料",
        "description": "月平均-地面測站資料",
        "parameters": [
          {
            "name": "Authorization",
            "required": True,
            "type": "string",
            "description": "氣象開放資料平台會員授權碼"
          },
          {
            "name": "limit",
            "required": False,
            "type": "number($int)",
            "description": "限制最多回傳的資料，預設為回傳全部筆數"
          },
          {
            "name": "offset",
            "required": False,
            "type": "number($int)",
            "description": "指定從第幾筆後開始回傳，預設為第 0 筆開始回傳"
          },
          {
            "name": "format",
            "required": False,
            "type": "string",
            "description": "回傳資料格式，預設為 json 格式Available values: JSON, XML--JSONXML"
          },
          {
            "name": "StationID",
            "required": False,
            "type": "array[string]",
            "description": "測站站號，請參考https://e-service.cwa.gov.tw/wdps/obs/state.htm，預設為全部回傳"
          },
          {
            "name": "weatherElement",
            "required": False,
            "type": "array[string]",
            "description": "要查詢的天氣要素Available values: AirPressure, AirTemperature, RelativeHumidity, CloudAmount, SunshineDuration, Precipitation, WindSpeed--AirPressureAirTemperatureRelativeHumidityCloudAmountSunshineDurationPrecipitationWindSpeed"
          },
          {
            "name": "Month",
            "required": False,
            "type": "array[integer]",
            "description": "要查詢的月份，查詢1回傳1月份資料，查詢2回傳2月份資料，依此類推Available values: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12--123456789101112"
          }
        ]
      },
      {
        "path": "/v1/rest/datastore/C-B0074-001",
        "dataId": "C-B0074-001",
        "summary": "氣象測站基本資料-有人氣象測站基本資料",
        "description": "氣象測站基本資料-有人氣象測站基本資料",
        "parameters": [
          {
            "name": "Authorization",
            "required": True,
            "type": "string",
            "description": "氣象開放資料平台會員授權碼"
          },
          {
            "name": "limit",
            "required": False,
            "type": "number($int)",
            "description": "限制最多回傳的資料，預設為回傳全部筆數"
          },
          {
            "name": "offset",
            "required": False,
            "type": "number($int)",
            "description": "指定從第幾筆後開始回傳，預設為第 0 筆開始回傳"
          },
          {
            "name": "format",
            "required": False,
            "type": "string",
            "description": "回傳資料格式，預設為 json 格式Available values: JSON, XML--JSONXML"
          },
          {
            "name": "StationID",
            "required": False,
            "type": "array[string]",
            "description": "測站站號，請參考https://e-service.cwa.gov.tw/wdps/obs/state.htm，預設為全部回傳"
          },
          {
            "name": "status",
            "required": False,
            "type": "array[string]",
            "description": "測站狀態Available values: 現存測站, 已撤銷--現存測站已撤銷"
          }
        ]
      },
      {
        "path": "/v1/rest/datastore/C-B0074-002",
        "dataId": "C-B0074-002",
        "summary": "氣象測站基本資料-無人氣象測站基本資料",
        "description": "氣象測站基本資料-無人氣象測站基本資料",
        "parameters": [
          {
            "name": "Authorization",
            "required": True,
            "type": "string",
            "description": "氣象開放資料平台會員授權碼"
          },
          {
            "name": "limit",
            "required": False,
            "type": "number($int)",
            "description": "限制最多回傳的資料，預設為回傳全部筆數"
          },
          {
            "name": "offset",
            "required": False,
            "type": "number($int)",
            "description": "指定從第幾筆後開始回傳，預設為第 0 筆開始回傳"
          },
          {
            "name": "format",
            "required": False,
            "type": "string",
            "description": "回傳資料格式，預設為 json 格式Available values: JSON, XML--JSONXML"
          },
          {
            "name": "StationID",
            "required": False,
            "type": "array[string]",
            "description": "測站站號，請參考https://e-service.cwa.gov.tw/wdps/obs/state.htm，預設為全部回傳"
          },
          {
            "name": "status",
            "required": False,
            "type": "array[string]",
            "description": "測站狀態Available values: 現存測站, 已撤銷--現存測站已撤銷"
          }
        ]
      }
    ]
  },
  "alert": {
    "cmd": "alert",
    "title": "天氣警特報",
    "apis": [
      {
        "path": "/v1/rest/datastore/W-C0033-001",
        "dataId": "W-C0033-001",
        "summary": "天氣特報-各別縣市地區目前之天氣警特報情形",
        "description": "天氣特報-各別縣市地區目前之天氣警特報情形",
        "parameters": [
          {
            "name": "Authorization",
            "required": True,
            "type": "string",
            "description": "氣象開放資料平台會員授權碼"
          },
          {
            "name": "limit",
            "required": False,
            "type": "number($int)",
            "description": "限制最多回傳的資料，預設為回傳全部筆數"
          },
          {
            "name": "offset",
            "required": False,
            "type": "number($int)",
            "description": "指定從第幾筆後開始回傳，預設為第 0 筆開始回傳"
          },
          {
            "name": "format",
            "required": False,
            "type": "string",
            "description": "回傳資料格式，預設為 json 格式Available values: JSON, XML--JSONXML"
          },
          {
            "name": "locationName",
            "required": False,
            "type": "array[string]",
            "description": "縣市名稱，預設為所有縣市Available values: 宜蘭縣, 花蓮縣, 臺東縣, 澎湖縣, 金門縣, 連江縣, 臺北市, 新北市, 桃園市, 臺中市, 臺南市, 高雄市, 基隆市, 新竹縣, 新竹市, 苗栗縣, 彰化縣, 南投縣, 雲林縣, 嘉義縣, 嘉義市, 屏東縣--宜蘭縣花蓮縣臺東縣澎湖縣金門縣連江縣臺北市新北市桃園市臺中市臺南市高雄市基隆市新竹縣新竹市苗栗縣彰化縣南投縣雲林縣嘉義縣嘉義市屏東縣"
          },
          {
            "name": "phenomena",
            "required": False,
            "type": "array[string]",
            "description": "當時發佈之警特報類型Available values: 濃霧, 大雨, 豪雨, 大豪雨, 超大豪雨, 陸上強風, 海上陸上颱風--濃霧大雨豪雨大豪雨超大豪雨陸上強風海上陸上颱風"
          }
        ]
      },
      {
        "path": "/v1/rest/datastore/W-C0033-002",
        "dataId": "W-C0033-002",
        "summary": "天氣特報-各別天氣警特報之內容及所影響之區域",
        "description": "天氣特報-各別天氣警特報之內容及所影響之區域",
        "parameters": [
          {
            "name": "Authorization",
            "required": True,
            "type": "string",
            "description": "氣象開放資料平台會員授權碼"
          },
          {
            "name": "limit",
            "required": False,
            "type": "number($int)",
            "description": "限制最多回傳的資料，預設為回傳全部筆數"
          },
          {
            "name": "offset",
            "required": False,
            "type": "number($int)",
            "description": "指定從第幾筆後開始回傳，預設為第 0 筆開始回傳"
          },
          {
            "name": "format",
            "required": False,
            "type": "string",
            "description": "回傳資料格式，預設為 json 格式Available values: JSON, XML--JSONXML"
          },
          {
            "name": "locationName",
            "required": False,
            "type": "array[string]",
            "description": "依照當時發佈特報之涵蓋區域市，區域名稱請詳見https://opendata.cwa.gov.tw/opendatadoc/Opendata_Warnings.pdf附錄 B『特報之影響區域名稱對照表』"
          },
          {
            "name": "phenomena",
            "required": False,
            "type": "array[string]",
            "description": "當時發佈之警特報類型Available values: 濃霧, 大雨, 豪雨, 大豪雨, 超大豪雨, 陸上強風, 颱風--濃霧大雨豪雨大豪雨超大豪雨陸上強風颱風"
          }
        ]
      },
      {
        "path": "/v1/rest/datastore/W-C0034-005",
        "dataId": "W-C0034-005",
        "summary": "颱風消息與警報-熱帶氣旋路徑",
        "description": "西北太平洋地區及南海目前所有活動中熱帶氣旋之資訊-熱帶性低氣壓及颱風過去、現在及未來預報之資訊",
        "parameters": [
          {
            "name": "Authorization",
            "required": True,
            "type": "string",
            "description": "氣象開放資料平台會員授權碼"
          },
          {
            "name": "limit",
            "required": False,
            "type": "number($int)",
            "description": "限制最多回傳的資料，預設為回傳全部筆數"
          },
          {
            "name": "offset",
            "required": False,
            "type": "number($int)",
            "description": "指定從第幾筆後開始回傳，預設為第 0 筆開始回傳"
          },
          {
            "name": "format",
            "required": False,
            "type": "string",
            "description": "回傳資料格式，預設為 json 格式Available values: JSON, XML--JSONXML"
          },
          {
            "name": "cwaTdNo",
            "required": False,
            "type": "number($int)",
            "description": "為熱帶性低氣壓編號，預設全部回傳"
          },
          {
            "name": "dataset",
            "required": False,
            "type": "array[string]",
            "description": "analysisData/forecastData，預設全部回傳Available values: analysisData, forecastData--analysisDataforecastData"
          },
          {
            "name": "fixTime",
            "required": False,
            "type": "array[string]",
            "description": "過去及現在定位時間，預設全部回傳, 格式為「yyyy-MM-ddThh:mm:ss」"
          },
          {
            "name": "tau",
            "required": False,
            "type": "array[number]",
            "description": "預報時距，預設全部回傳 輸入數字6~120 可輸入多筆資料，用逗號分隔"
          },
          {
            "name": "timeFrom",
            "required": False,
            "type": "string($date)",
            "description": "時間區段，針對analysisData篩選需要之時間區段，時間從「timeFrom」 開始篩選，直到內容之最後時間，並可與參數 「timeTo」 合併使用格式為「yyyy-MM-ddThh:mm:ss」，若使用參數「fix_time」，則參數「timeFrom」的篩選資料則會失效，預設為全部回傳"
          },
          {
            "name": "timeTo",
            "required": False,
            "type": "string($date)",
            "description": "時間區段，針對analysisData篩選需要之時間區段，時間從內容之最初時間開始篩選，直到 timeTo，並可與參數 「timeFrom」 合併使用格式為「yyyy-MM-ddThh:mm:ss」，若使用「fix_time」，則參數「timeTo」的篩選資料則會失效，預設為全部回傳"
          },
          {
            "name": "sort",
            "required": False,
            "type": "array[string]",
            "description": "對「cwaTdNo」進行升冪排序, 預設不排序Available values: cwaTdNo--cwaTdNo"
          }
        ]
      }
    ]
  },
  "health": {
    "cmd": "health",
    "title": "數值預報",
    "apis": [
      {
        "path": "/v1/rest/datastore/M-A0085-001",
        "dataId": "M-A0085-001",
        "summary": "健康氣象-熱傷害指數及警示全台各鄉鎮五日逐三小時預報",
        "description": "健康氣象相關數值預報資料-熱傷害分級與綜合溫度熱指數",
        "parameters": [
          {
            "name": "Authorization",
            "required": True,
            "type": "string",
            "description": "氣象開放資料平台會員授權碼"
          },
          {
            "name": "limit",
            "required": False,
            "type": "number($int)",
            "description": "限制最多回傳的資料, 預設為回傳全部筆數"
          },
          {
            "name": "offset",
            "required": False,
            "type": "number($int)",
            "description": "指定從第幾筆後開始回傳, 預設為第 0 筆開始回傳"
          },
          {
            "name": "format",
            "required": False,
            "type": "string",
            "description": "回傳資料格式, 預設為 json 格式Available values: JSON, XML--JSONXML"
          },
          {
            "name": "CountyName",
            "required": False,
            "type": "array[string]",
            "description": "各縣市名稱，預設為全部回傳Available values: 宜蘭縣, 花蓮縣, 臺東縣, 澎湖縣, 金門縣, 連江縣, 臺北市, 新北市, 桃園市, 臺中市, 臺南市, 高雄市, 基隆市, 新竹縣, 新竹市, 苗栗縣, 彰化縣, 南投縣, 雲林縣, 嘉義縣, 嘉義市, 屏東縣--宜蘭縣花蓮縣臺東縣澎湖縣金門縣連江縣臺北市新北市桃園市臺中市臺南市高雄市基隆市新竹縣新竹市苗栗縣彰化縣南投縣雲林縣嘉義縣嘉義市屏東縣"
          },
          {
            "name": "TownName",
            "required": False,
            "type": "array[string]",
            "description": "各縣市所對應鄉鎮名稱，請參考https://opendata.cwa.gov.tw/opendatadoc/Opendata_City.pdf，附錄 A『全臺縣市鄉鎮對照表』，預設為全部回傳"
          },
          {
            "name": "WeatherElements",
            "required": False,
            "type": "array[string]",
            "description": "天氣預報因子，預設為全部回傳Available values: HeatInjuryIndex, HeatInjuryWarning--HeatInjuryIndexHeatInjuryWarning"
          },
          {
            "name": "IssueTime",
            "required": False,
            "type": "array[string]",
            "description": "時間因子，預設全部回傳，格式為「yyyy-MM-ddThh:mm:ss」"
          },
          {
            "name": "timeFrom",
            "required": False,
            "type": "string($date)",
            "description": "時間區段，篩選需要之時間區段，時間從「timeFrom」 開始篩選，直到內容之最後時間，並可與參數 「timeTo」 合併使用，格式為「yyyy-MM-ddThh:mm:ss」若使用參數「dataTime」，則參數「timeFrom」的篩選資料則會失效，預設為全部回傳"
          },
          {
            "name": "timeTo",
            "required": False,
            "type": "string($date)",
            "description": "時間區段，篩選需要之時間區段，時間從內容之最初時間開始篩選，直到 timeTo，並可與參數 「timeFrom」 合併使用，格式為「yyyy-MM-ddThh:mm:ss」若使用「IssueTime」，則參數「timeTo」的篩選資料則會失效，預設為全部回傳"
          },
          {
            "name": "sort",
            "required": False,
            "type": "array[string]",
            "description": "「IssueTime」 為針對「IssueTime」，預設不排序Available values: IssueTime--IssueTime"
          }
        ]
      }
    ]
  },
  "astronomy": {
    "cmd": "astronomy",
    "title": "天文",
    "apis": [
      {
        "path": "/v1/rest/datastore/A-B0062-001",
        "dataId": "A-B0062-001",
        "summary": "日出日沒時刻-全臺各縣市年度逐日日出日沒時刻資料",
        "description": "全臺各縣市每天的日出、日沒及太陽過中天等時刻資料含有日出日沒時之方位及過中天時之仰角資料",
        "parameters": [
          {
            "name": "Authorization",
            "required": True,
            "type": "string",
            "description": "氣象開放資料平台會員授權碼"
          },
          {
            "name": "limit",
            "required": False,
            "type": "number($int)",
            "description": "限制最多回傳的資料, 預設為回傳全部筆數"
          },
          {
            "name": "offset",
            "required": False,
            "type": "number($int)",
            "description": "指定從第幾筆後開始回傳, 預設為第 0 筆開始回傳"
          },
          {
            "name": "format",
            "required": False,
            "type": "string",
            "description": "回傳資料格式, 預設為 json 格式Available values: JSON, XML--JSONXML"
          },
          {
            "name": "CountyName",
            "required": False,
            "type": "array[string]",
            "description": "臺灣各縣市, 預設為回傳全部縣市Available values: 宜蘭縣, 花蓮縣, 臺東縣, 澎湖縣, 金門縣, 連江縣, 臺北市, 新北市, 桃園市, 臺中市, 臺南市, 高雄市, 基隆市, 新竹縣, 新竹市, 苗栗縣, 彰化縣, 南投縣, 雲林縣, 嘉義縣, 嘉義市, 屏東縣--宜蘭縣花蓮縣臺東縣澎湖縣金門縣連江縣臺北市新北市桃園市臺中市臺南市高雄市基隆市新竹縣新竹市苗栗縣彰化縣南投縣雲林縣嘉義縣嘉義市屏東縣"
          },
          {
            "name": "Date",
            "required": False,
            "type": "array[string]",
            "description": "時間因子, 格式為「yyyy-MM-dd」, 最多回傳180筆資料預設回傳內容之最初180筆的資料"
          },
          {
            "name": "parameter",
            "required": False,
            "type": "array[string]",
            "description": "預報因子，預設為全部回傳Available values: BeginCivilTwilightTime, SunRiseTime, SunRiseAZ, SunTransitTime, SunTransitAlt, SunSetTime, SunSetAZ, EndCivilTwilightTime--BeginCivilTwilightTimeSunRiseTimeSunRiseAZSunTransitTimeSunTransitAltSunSetTimeSunSetAZEndCivilTwilightTime"
          },
          {
            "name": "timeFrom",
            "required": False,
            "type": "string($date)",
            "description": "時間區段,篩選需要之時間區段,格式為「yyyy-MM-dd」時間從「timeFrom」開始篩選,直到「timeFrom」之後180天的資料可與參數 「timeTo」 合併使用,時間從「timeFrom」開始篩選,直到「timeTo」,可回傳最多180天長度的資料在合併使用參數「timeTo」和參數「timeFrom」的時候，若是 「timeTo」的時間超過「timeFrom」之後180天，則僅會回傳「timeFrom」開始直到「timeFrom」之後180天之間的資料若使用參數「Date」,則參數「timeFrom」的篩選資料則會失效若是參數「timeFrom」和參數「timeTo」都沒有設定，預設會回傳內容中最初180筆的資料"
          },
          {
            "name": "timeTo",
            "required": False,
            "type": "string($date)",
            "description": "時間區段, 篩選需要之時間區段,格式為「yyyy-MM-dd」時間從「timeTo」之前180天開始篩選,直到「timeTo」可與參數「 timeFrom」 合併使用,時間從「timeFrom」開始篩選,直到「timeTo」,可回傳最多180天長度的資料在合併使用參數「timeTo」和參數「timeFrom」的時,若是 「timeTo」的時間超過「timeFrom」之後180天,則僅會回傳「timeFrom」開始直到「timeFrom」之後180天之間的資料若使用參數「Date」,則參數「timeTo」的篩選資料則會失效若是參數「timeFrom」和參數「timeTo」都沒有設定,預設會回傳內容中最初180筆的資料"
          },
          {
            "name": "sort",
            "required": False,
            "type": "array[string]",
            "description": "對「CountyName」或「Date」進行升冪排序, 預設不排序Available values: CountyName, Date--CountyNameDate"
          }
        ]
      },
      {
        "path": "/v1/rest/datastore/A-B0063-001",
        "dataId": "A-B0063-001",
        "summary": "月出月沒時刻-全臺各縣市年度逐日月出月沒時刻資料",
        "description": "全臺各縣市每天的月出、月沒及月球過中天等時刻資料含有月出月沒時之方位及過中天時之仰角資料",
        "parameters": [
          {
            "name": "Authorization",
            "required": True,
            "type": "string",
            "description": "氣象開放資料平台會員授權碼"
          },
          {
            "name": "limit",
            "required": False,
            "type": "number($int)",
            "description": "限制最多回傳的資料, 預設為回傳全部筆數"
          },
          {
            "name": "offset",
            "required": False,
            "type": "number($int)",
            "description": "指定從第幾筆後開始回傳, 預設為第 0 筆開始回傳"
          },
          {
            "name": "format",
            "required": False,
            "type": "string",
            "description": "回傳資料格式, 預設為 json 格式Available values: JSON, XML--JSONXML"
          },
          {
            "name": "CountyName",
            "required": False,
            "type": "array[string]",
            "description": "臺灣各縣市, 預設為回傳全部縣市Available values: 宜蘭縣, 花蓮縣, 臺東縣, 澎湖縣, 金門縣, 連江縣, 臺北市, 新北市, 桃園市, 臺中市, 臺南市, 高雄市, 基隆市, 新竹縣, 新竹市, 苗栗縣, 彰化縣, 南投縣, 雲林縣, 嘉義縣, 嘉義市, 屏東縣--宜蘭縣花蓮縣臺東縣澎湖縣金門縣連江縣臺北市新北市桃園市臺中市臺南市高雄市基隆市新竹縣新竹市苗栗縣彰化縣南投縣雲林縣嘉義縣嘉義市屏東縣"
          },
          {
            "name": "Date",
            "required": False,
            "type": "array[string]",
            "description": "時間因子, 格式為「yyyy-MM-dd」, 最多回傳180筆資料預設回傳內容之最初180筆的資料"
          },
          {
            "name": "parameter",
            "required": False,
            "type": "array[string]",
            "description": "預報因子，預設為全部回傳Available values: MoonRiseTime, MoonRiseAZ, MoonTransitTime, MoonTransitAlt, MoonSetTime, MoonSetAZ--MoonRiseTimeMoonRiseAZMoonTransitTimeMoonTransitAltMoonSetTimeMoonSetAZ"
          },
          {
            "name": "timeFrom",
            "required": False,
            "type": "string($date)",
            "description": "時間區段,篩選需要之時間區段,格式為「yyyy-MM-dd」時間從「timeFrom」開始篩選,直到「timeFrom」之後180天的資料並可與參數 「timeTo」 合併使用,時間從「timeFrom」開始篩選,直到「timeTo」,可回傳最多180天長度的資料在合併使用參數「timeTo」和參數「timeFrom」的時候,若是 「timeTo」的時間超過「timeFrom」之後180天,則僅會回傳「timeFrom」開始直到「timeFrom」之後180天之間的資料若使用參數「Date」,則參數「timeFrom」的篩選資料則會失效若是參數「timeFrom」和參數「timeTo」都沒有設,預設會回傳內容中最初180筆的資料"
          },
          {
            "name": "timeTo",
            "required": False,
            "type": "string($date)",
            "description": "時間區段, 篩選需要之時間區段,格式為「yyyy-MM-dd」時間從「timeTo」之前180天開始篩選,直到「timeTo」並可與參數 「timeFrom」 合併使用,時間從「timeFrom」開始篩選,直到「timeTo」,可回傳最多180天長度的資料在合併使用參數「timeTo」和參數「timeFrom」的時候,若是 「timeTo」的時間超過「timeFrom」之後180天,則僅會回傳「timeFrom」開始直到「timeFrom」之後180天之間的資料若使用參數「Date」,則參數「timeTo」的篩選資料則會失效若是參數「timeFrom」和參數「timeTo」都沒有設定,預設會回傳內容中最初180筆的資料"
          },
          {
            "name": "sort",
            "required": False,
            "type": "array[string]",
            "description": "對「CountyName」或「Date」進行升冪排序, 預設不排序Available values: CountyName, Date--CountyNameDate"
          }
        ]
      }
    ]
  }
}