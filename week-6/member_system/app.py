#中文顯示
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

#---------------------------讀取.env的環境變數---------------------------------------------------------------------#
import os
from dotenv import load_dotenv
import MySQLdb

load_dotenv()
connection = MySQLdb.connect(
    host=os.getenv("MYSQL_HOST"),
    user=os.getenv("MYSQL_USER"),
    passwd=os.getenv("MYSQL_PASSWORD"),
    db=os.getenv("MYSQL_DATABASE"),
    charset=os.getenv("charset") #加這一行(utf8)可以不會讓中文變亂碼
)

#----------------------python MySQL資料庫---------------------------------------------------------------------------
import mysql.connector   #載入MSQL

#連線到MySQL資料庫
cursor = connection.cursor() # 獲取操作游標，也就是開始操作
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
    #使⽤者進入會員頁面member.html，後端程式向資料庫取得所有留⾔內容，顯⽰在會員⾴⾯的最下⽅。
    #使⽤ SELECT 搭配 JOIN 語法，取得所有留⾔，結果須包含留⾔者會員的姓名。
    cursor.execute("SELECT member.name,message.content FROM member INNER JOIN message ON member.id =message.member_id")
    name_message_array = cursor.fetchall()

    #檢查是否成曾經登入過，進行權限控管
    if "name" in session: #驗證成功後，在 Flask Session 中記錄使⽤者狀態為已登入，導向member.html
        return render_template("member.html",name= session["name"]
                                             #把所有留⾔者的名字和留言內容傳到前端
                                            ,name_message_array= name_message_array)
    else:
        return redirect("/") #使⽤者狀態若為未登入，必須直接導向到⾸⾴，不顯⽰登入後的網⾴內容

#錯誤頁面error.html    /error?msg=錯誤訊息 
@app.route("/error")
def error():
    message = request.args.get("msg","發生錯誤請聯繫客服")
    return render_template("error.html", message = message)

#會員頁面member.html的註冊/signup功能
@app.route("/signup",methods=["POST"])
def signup():
    #從前端接收資料
    name =request.form["name"]
    username=request.form["username"]
    password =request.form["password"]

    #檢查member表中username欄位是否有相同username的資料
    cursor.execute("SELECT * FROM member WHERE username = %s",(username))
    result = cursor.fetchone() 
    
    #如果找到相同username的話，導向error頁面並顯示帳號已經被註冊
    if result != None:
        return redirect("/error?msg=帳號已經被註冊")

    #如果沒有找到相同username的話，則將資料插入資料庫完成註冊並且將使用者導回首頁
    insert_to_membertable = "INSERT INTO member (name, username, password)  VALUES ( %s, %s, %s)"
    val_membertable = (name,username,password)
    cursor.execute(insert_to_membertable, val_membertable)
    connection.commit() # 確保數據已提交到數據庫
    
    return redirect("/")

#會員頁面member.html的登入/signin功能
@app.route("/signin",methods=["POST"])
def signin():
    #從前端接收資料
    username =request.form["username"]
    password =request.form["password"]
    
    #根據接收到的資料跟資料庫作互動
    cursor.execute("SELECT * FROM member WHERE username = %s AND password = %s",(username,password,))
    result = cursor.fetchone()

    #如果找不到對應資料將導向錯誤頁面
    if (result == None) and (len(username) or len(password) > 0):
        return redirect("/error?msg=帳號、或密碼輸入錯誤")
    if (len(username) or len(password)) == 0:
        return redirect("/error?msg=請輸入帳號、密碼")
    
    #登入成功，如果有對應資料就在Seesion紀錄會員資訊，導向會員頁面
    session["name"] = result[1] #result[1]內存的是name欄位
    return redirect("/member")

#會員頁面member.html的登出/signout功能
@app.route("/signout")
def signout():
    #移除session中的會員資訊
    del session["name"]
    return redirect("/")

#會員頁面member.html的留言/message功能
@app.route("/message",methods=["POST"])
def message():
    #從前端接收新留言
    content =request.form["content"]

    #從收到的新留言的session["name"]去查member表的id
    name= session["name"]
    cursor.execute("SELECT * FROM member WHERE name = %s",(name,))
    result = cursor.fetchone() 
    member_id= result[0] #result[0]內存的是member表的id欄位，對到message表的member_id欄位

    #將上面得到的member表的id欄位和從前端得到的留言插入資料庫的message表member_id欄位和content欄位
    insert_to_messagetable = "INSERT INTO message (member_id,content)  VALUES ( %s, %s)"
    val_messagetable = (member_id,content)
    cursor.execute(insert_to_messagetable, val_messagetable)
    connection.commit() # 確保數據已提交到數據庫
    
    return redirect("/member")


#啟動網站的伺服器，透過port參數指定port number
if __name__ == "__main__":
    app.run(port=4000) 

