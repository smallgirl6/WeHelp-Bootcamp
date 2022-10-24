<h1>歡迎光臨，請註冊登入系統</h1>

後端用Python flask加上MySQL資料庫<br/>
<br/>
前端用HTML加上CSS<br/>
</br>
1.　首頁
</br>
</br>
![image](https://user-images.githubusercontent.com/111422800/197567767-ecc49610-62a9-4217-a36d-bb36f51beaeb.png) </br>
2.　會員頁面
</br>
</br>
![image](https://user-images.githubusercontent.com/111422800/197575579-74ec5a7e-6d67-4513-92b7-68473d6d76f7.png)</br>
3.　錯誤頁面
</br>
</br>
![image](https://user-images.githubusercontent.com/111422800/197577026-79f7e4e5-90f4-4e35-b81c-1bd3a9e8e26a.png)
</br>
</br>

<h2>註冊帳號</h2>

1.　若資料庫沒有相同的帳號且都有正確輸入，那就把使用者輸入資料放入資料庫
</br>
</br>
![image](https://user-images.githubusercontent.com/111422800/197567490-99902199-3d9c-4018-b1ef-08eb3dbf3352.png)</br>
![image](https://user-images.githubusercontent.com/111422800/197566997-4004187c-21ba-471c-a92d-34b6796155fc.png)</br>
</br>
2.　如果資料庫已經有相同的帳號，那就導向error頁面，並顯示帳號已經被註冊
</br>
</br>
![image](https://user-images.githubusercontent.com/111422800/197567284-3e03ad2f-6349-4708-b623-b242cd584c17.png)
![image](https://user-images.githubusercontent.com/111422800/197567609-7311716a-50e9-47a8-9467-626770e06a31.png)</br>
</br>
3.　姓名、帳號、密碼全部不可以空白，其中一個空白那就導向error頁面，並顯示請輸入姓名、帳號、密碼
</br>
![image](https://user-images.githubusercontent.com/111422800/197570955-2d53b6b2-12f9-469a-b5b9-4ae6b7c42988.png)
![image](https://user-images.githubusercontent.com/111422800/197571030-fc740004-a030-430c-b36b-83e9809fd549.png)</br>
![image](https://user-images.githubusercontent.com/111422800/197571153-2c7ec9cf-993c-40ef-9225-ba9a63f19094.png)
![image](https://user-images.githubusercontent.com/111422800/197571030-fc740004-a030-430c-b36b-83e9809fd549.png)</br>
</br>

<h2>登入系統</h2>

1.　若輸入的帳號和密碼和資料庫的帳密相同的話，就將使⽤者編號、姓名等資訊加入 Session 中紀錄，並導向member頁面並顯示使用者的名字
</br>
</br>
![image](https://user-images.githubusercontent.com/111422800/197573646-de73d57e-283f-4b0d-ac98-8407b8cb3e90.png)
![image](https://user-images.githubusercontent.com/111422800/197575364-a2e476b6-f408-4401-afd1-7e5ddf04f500.png)</br>
</br>
2.　若輸入的帳號和密碼和資料庫的帳密不相同的話，登入失敗，將使⽤者導向向error頁面，並顯⽰「帳號或密碼輸入錯誤」
</br>
</br>
![image](https://user-images.githubusercontent.com/111422800/197574129-ff22e72e-5de2-4f46-9a52-4f02d03f30b7.png)
![image](https://user-images.githubusercontent.com/111422800/197574199-37279e25-4fd8-41d4-b2e0-27c53644336f.png)</br>
</br>
3.　帳號、密碼兩個都空白的話，那就導向error頁面，並顯示請輸入帳號、密碼
</br>
</br>
![image](https://user-images.githubusercontent.com/111422800/197574531-6a1784e9-b625-45c6-b555-970dec7e10d1.png)
![image](https://user-images.githubusercontent.com/111422800/197574601-83f17010-41e0-46fc-9088-9922d7a1cd76.png)</br>
</br>
</br>

<h2>登出系統</h2>

1.　使⽤者登入帳⼾後，可以在會員⾴⾯點擊登出帳⼾，並刪除 Session 中紀錄，導向首頁
</br>
</br>
![image](https://user-images.githubusercontent.com/111422800/197577602-4a40d7ce-f0c8-4459-bb48-3cfbe3ca1d23.png)
![image](https://user-images.githubusercontent.com/111422800/197578018-7b497140-daa4-47dc-a784-a4d33de66b7c.png)</br>
</br>
</br>

<h2>留言系統</h2>

1.　使⽤者登入帳⼾後，可以在會員⾴⾯加入留言，新加入的留言會加到資料庫後並顯示在下方
</br>
</br>
![image](https://user-images.githubusercontent.com/111422800/197578605-99dfa366-fc6c-4fa9-88c0-3a30d171f251.png)</br>
![image](https://user-images.githubusercontent.com/111422800/197578809-b1d72edb-e893-4809-bf89-6a8aad987174.png)</br>
資料庫端</br>
![image](https://user-images.githubusercontent.com/111422800/197579018-ad783579-c820-4019-9654-d1c90aa0d5d2.png)





