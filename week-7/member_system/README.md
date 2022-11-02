<h1>歡迎光臨，請註冊登入系統</h1>
<b>後端用Python flask加上MySQL資料庫<b><br/>
<br/>
<b>前端用HTML加上CSS加上JAVASCRIPT<b><br/>
</br>

  1.　首頁
</br>
</br>
![image](https://user-images.githubusercontent.com/111422800/197567767-ecc49610-62a9-4217-a36d-bb36f51beaeb.png) </br>

2.　會員頁面
</br>
</br>
![image](https://user-images.githubusercontent.com/111422800/199562152-b702699f-19a5-4aba-8aa1-3fd40ae0206f.png)　</br>

<h2>後端建立查詢會員資料的 API</h2>

1.　在後端建立查詢會員資料的 API後，用postman確認資料
</br>
</br>
2.　mysql資料庫，用小班尼來試看看 
</br>
</br>
![image](https://user-images.githubusercontent.com/111422800/199563289-32613ee9-6759-43b8-9539-68c3abe62a56.png)
</br>
</br>
3.　postman的結果 http://127.0.0.1:3000/api/member?username=Benny001
</br>
</br>
![image](https://user-images.githubusercontent.com/111422800/199563803-54dc83ad-7c3a-4288-867a-5cb9535ae4c3.png)
</br>
</br>
4.　用不存在的使用者測試的後，postman的結果 http://127.0.0.1:3000/api/member?username=ply
</br>
</br>
![image](https://user-images.githubusercontent.com/111422800/199564202-4bfe168f-632e-4c36-b76f-4159da4bafae.png)
</br>
</br>

<h2>前端透過 Fetch 連接 API 查詢會員資料，並顯示在畫面上</h2>

1.　輸入會員帳號並按下查詢會員姓名後，下面會顯示會員姓名和帳號
</br>
</br>

2.　用MYtestaccount這組帳號測試看看
</br>
</br>
![image](https://user-images.githubusercontent.com/111422800/199566457-21afdb12-56bd-4554-9c53-65d2c9e3a243.png)
</br>
</br>

3.　用一個不存在的使用者帳號試看看，會顯示查無此人
</br>
</br>
![image](https://user-images.githubusercontent.com/111422800/199566936-485ab380-0511-4516-84c0-2bfac27c81c5.png)
</br>
</br>
<h2>修改姓名功能</h2>
</br>
</br>

1.　輸入想變更的姓名，原本叫阿花，想改名為吳水仙
</br>
</br>
![image](https://user-images.githubusercontent.com/111422800/199567664-b9e3dcd9-eff8-405b-a7ca-57e398878202.png)
</br>
</br>

2.　成功更新後下面會顯示「更新成功」，歡迎光臨那邊也會顯示成更新後的姓名
</br>
</br>
![image](https://user-images.githubusercontent.com/111422800/199568307-82c5b8d1-4d35-4e92-a941-14c8a627dbd0.png)
</br>
</br>

3.　確認資料庫是否也被變更，可以發現資料庫也已經由阿花改成吳水仙了
</br>
</br>

![image](https://user-images.githubusercontent.com/111422800/199569318-187a5801-fc88-459c-a4f6-7b31431994c5.png)
</br>
</br>

4.　如果不輸入姓名直接按下更新button的話會回傳「更新失敗」
</br>
</br>
![image](https://user-images.githubusercontent.com/111422800/199569925-4dec4b2d-5459-4244-abc0-89003ddf7606.png)
</br>
</br>

5.　資料庫也不會被變更
</br>
</br>
![image](https://user-images.githubusercontent.com/111422800/199569318-187a5801-fc88-459c-a4f6-7b31431994c5.png)
</br>
</br>
