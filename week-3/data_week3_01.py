import csv
import urllib.request as request
import json


src="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json" 
with request.urlopen(src) as response:
    # data=response.read().decode("utf-8")
    data=json.load(response)  #JSON模組處理JSON格式

#將地點名稱列出來
    places= data["result"]["results"] #列表

#把資料寫到筆記本裡
with open("data.csv","w",newline="",encoding="utf-8") as f:
        for place in places:
            if int(place["xpostDate"][0:4]) >= 2015: #根據 xpostDate 欄位，僅輸出 2015 年以後 ( 包含 2015 年 ) 的資料 這邊擷取前4個數字
                
                # print(place["file"][0:(place["file"].lower().find(".jpg"))+4]) 
                # 找出每一個項目的第一張圖 (先先找出第一個..jpg的位置，在指定範圍從開頭列印到.jpg，加4是因為要讓.jpg也加進網址列)
                # 發現有兩個大寫JPG沒被印出來所以用.lower()把它忽略大小寫
                writer = csv.writer(f)
                write_to= (place["stitle"], place["address"][5:8], place["longitude"], place["latitude"], place["file"][0:(place["file"].lower().find(".jpg"))+4])
                writer.writerow(write_to)