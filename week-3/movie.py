#pip install beautifulsoup4import urllib.request as request
#中文顯示
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import urllib.request as  req

#一、函數
def getdata(getsrc):
    #建一個Request物件 添加Request headers資訊
    request = req.Request(getsrc,headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
    })

    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")

    #解析原始碼，取得每篇文章標題
    import bs4     
    root = bs4.BeautifulSoup(data,"html.parser")  #BeautifulSoup可協助解析html格式文件
    titles=root.find_all("div",class_="title") #尋找所有class="title"的div標籤
    
    All_Array = [] #如果標題有a標籤(沒被刪除)那就存進去

    for title in titles:
        if (title.a != None):
            All_Array.append(title.a.string) 
    
    Good_thunder_Array = []   #標題的前4個字若是 [好雷] 的話就存進去
    Normal_thunder_Array = [] #標題的前4個字若是 [普雷] 的話就存進去
    Bad_thunder_Array = []    #標題的前4個字若是 [負雷] 的話就存進去
    
    for i in All_Array:
        if i[0:4]=="[好雷]":
            Good_thunder_Array.append(i)
        if i[0:4]=="[普雷]":
            Normal_thunder_Array.append(i)
        if i[0:4]=="[負雷]":
            Bad_thunder_Array.append(i)
           
    nextLink = root.find("a",string="‹ 上頁") #找到內文是‹ 上頁的a標籤
    #傳回①.‹ 上頁的a標籤內的["href"]網址 ②好雷Array ③普雷Array ④負雷Array
    return nextLink["href"],Good_thunder_Array,Normal_thunder_Array,Bad_thunder_Array
    
    
#二、函式外的處理

Good_thunder_Array = []
Normal_thunder_Array = []
Bad_thunder_Array = []

pageURL="https://www.ptt.cc/bbs/movie/index.html"  

count=0
#做一個pageURL_Array裡面存放的第一筆是首頁，第二筆是開始是 getdata(pageURL)[0] 傳回來得網址
pageURL_Array= ["/bbs/movie/index.html"]

while count<10:
    pageURL= "https://www.ptt.cc"+ pageURL_Array[count] #把pageURL_Array內存的網址一筆筆的傳到pageURL
    pageURL_Array.append(getdata(pageURL)[0]) #當第一筆/bbs/movie/index.html船進去以後就可以透過 getdata(pageURL)[0] 得到第二筆，把它存到pageURL_Array讓上行code調用 
    Good_thunder_Array.append(getdata(pageURL)[1])   # getdata(pageURL)[1] 傳回來的Good_thunder_Array放入函式外面的Good_thunder_Array
    Normal_thunder_Array.append(getdata(pageURL)[2]) # getdata(pageURL)[2] 傳回來的Good_thunder_Array放入函式外面的Normal_thunder_Array
    Bad_thunder_Array.append(getdata(pageURL)[3])    # getdata(pageURL)[3] 傳回來的Good_thunder_Array放入函式外面的Bad_thunder_Array
    count+=1

#不一定每一頁都抓得到好雷或普雷之類的數據，如果沒有數據的話會回傳空Array[]，所以我只要不是空Array的值
Good_thunder_Array = [i for i in Good_thunder_Array  if i != []]     
Normal_thunder_Array = [i for i in Normal_thunder_Array  if i  != []]
Bad_thunder_Array = [i for i in Bad_thunder_Array  if i  != []]

#三、把資料寫到筆記本裡
with open("movie.txt","w",encoding="utf-8") as file:
    #由於每一頁抓出來的數據會變成一個小array存在各個大的array中，所以讀出每個大array的小array中
    for i in Good_thunder_Array: # i是小array
        for j in i:              # j是小array內的數據
            file.write(j+"\n")
        
    for i in Normal_thunder_Array:
        for j in i:
            file.write(j+"\n")
        
    for i in Bad_thunder_Array:
        for j in i:
            file.write(j+"\n")
        
   
    

    
