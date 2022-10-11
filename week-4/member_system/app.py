
#中文顯示

import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

#----------------------python flask mongo資料庫----------------------------------------------------

import pymongo #載入 pymongo物件

#連線到MongoDB雲端資料庫
client = pymongo.MongoClient("mongodb+srv://Hyggenini:@mycluster.nptn3ho.mongodb.net/?retryWrites=true&w=majority")
#把資料放到資料庫中
db = client.mywebsite #選擇操作mywebsite資料庫
print("資料庫連線建立成功")

#----------------------python flask網站後端----------------------------------------------------------

from flask import * #import flask全部模組

app = Flask(
    __name__,
    static_folder= "static", #靜態檔案的資料夾名稱
    static_url_path ="/"   #靜態檔案對應的網址路徑     
)    
app.secret_key="gogogo"  #為了使用Sessions，必須設置一個密鑰

#處理路由
#首頁index.html
@app.route("/")
def index():
    return render_template("index.html")

#會員頁面member.html
@app.route("/member")
def member():
    #檢查是否成曾經登入過，進行權限控管
    if "account" in session: #驗證成功後，在 Flask Session 中記錄使⽤者狀態為已登入，導向member.html

        return render_template("member.html",account= session["account"])
    else:
        return redirect("/") #使⽤者狀態若為未登入，必須直接導向到【⾸⾴】，不顯⽰登入後的網⾴內容。

#錯誤頁面error.html    /error?msg=錯誤訊息 
@app.route("/error")
def error():
    message = request.args.get("msg","發生錯誤請聯繫客服")
    return render_template("error.html", message = message)

#會員頁面member.html的註冊/signin功能
@app.route("/signin",methods=["POST"])
def signin():
    #從前端接收資料
    account =request.form["account"]
    password =request.form["password"]
    
    #根據接收到的資料跟資料庫作互動
    collection = db.users  #操作users集合
    result = collection.find_one({
    "$and":[
        {"account":account},
        {"password":password}
    ]    
    })

    #如果找不到對應資料將導向錯誤頁面
    if (result == None) and (len(account) or len(password) > 0):
        return redirect("/error?msg=帳號、或密碼輸入錯誤")
    if (len(account) or len(password)) == 0:
        return redirect("/error?msg=請輸入帳號、密碼")
    
    #登入成功，如果有對應資料就在Seesion紀錄會員資訊，導向會員頁面
    session["account"] = result["account"]
    return redirect("/member")

#會員頁面member.html的註冊/signout功能
@app.route("/signout")
def signout():
    #移除session中的會員資訊
    del session["account"]
    return redirect("/")

#會員頁面member.html的計算，建立路徑/square對應的處理函式
@app.route("/square")
def square():
    number = request.args.get("num","")
    number = int(number)
    square_number = number * number 
    #把結果回傳到square.html網站
    return render_template("square.html",result=square_number) 

#啟動網站的伺服器，透過port參數指定port number
app.run(port=3000) 

