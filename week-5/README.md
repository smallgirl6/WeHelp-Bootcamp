<h2>要求三：SQL CRUD</h2>

1.　使⽤ INSERT 指令新增⼀筆資料到 member 資料表中，這筆資料的 username 和password 欄位必須是 test。接著繼續新增⾄少 4 筆隨意的資料。</br>
    
     INSERT INTO member(id,name,username,password,follower_count,time) VALUES(1,"Jerry","test","test",90,"2022-08-30 08:00:00");</br>
    
     INSERT INTO member(name,username,password,follower_count,time) VALUES("Ken","Ken001","cc121",100,"2022-08-25 06:00:00");</br>
    
     INSERT INTO member(name,username,password,follower_count,time) VALUES("Sun","Sun001","bb221",99,"2022-09-28 15:00:00");</br>
     
     INSERT INTO member(name,username,password,follower_count,time) VALUES("Benny","Benny001","ac131",200,"2022-10-15 23:00:00");</br>
     
     INSERT INTO member(name,username,password) VALUES("Lucca","Lucca001","cc121");`</br>

![image](https://user-images.githubusercontent.com/111422800/196072999-f4039655-c790-419a-af32-27b0bec17cde.png)


2.　使⽤ SELECT 指令取得所有在 member 資料表中的會員資料。</br>
    
    SELECT * FROM member;
    
![image](https://user-images.githubusercontent.com/111422800/196073085-0a8567a5-1247-4a48-a8d5-831b341e61c7.png)


3.　使⽤ SELECT 指令取得所有在 member 資料表中的會員資料，並按照 time 欄位，由近到遠排序。</br>
    
    SELECT * FROM member ORDER BY time desc;</br>

![image](https://user-images.githubusercontent.com/111422800/196073677-72f2eac3-f7c1-4e1c-b56b-b92fe421b003.png)


4.　使⽤ SELECT 指令取得 member 資料表中第 2 ~ 4 共三筆資料，並按照 time 欄位，由近到遠排序。( 並非編號 2、3、4 的資料，⽽是排序後的第 2 ~ 4 筆資料 )。</br>
    
    SELECT * FROM member ORDER BY time desc LIMIT 1,3;</br>
    
 ![image](https://user-images.githubusercontent.com/111422800/196074759-3608f99b-efa1-4e90-9e4a-cbea148f1b8b.png)
 
5.　使⽤ SELECT 指令取得欄位 username 是 test 的會員資料。</br>

    SELECT * FROM member WHERE username="test" ;
  
 ![image](https://user-images.githubusercontent.com/111422800/196077859-69d84055-78cd-4a6d-bc90-ca8641cf28fb.png)


6.　使⽤ SELECT 指令取得欄位 username 是 test、且欄位 password 也是 test 的資料。</br>
    
    SELECT * FROM member WHERE username="test" && password="test" ;
    
![image](https://user-images.githubusercontent.com/111422800/196078096-d29d437f-6ab3-4937-ba5e-73ec0687bf4a.png)


7.　使⽤ UPDATE 指令更新欄位 username 是 test 的會員資料，將資料中的 name 欄位改成 test2。</br>
    
    SET SQL_SAFE_UPDATES = 0;

    
    PDATE member SET name="test2" WHERE username="test";

    
    UPDATE member SET name="test2" WHERE username="test";

    
    SELECT * FROM member;
    
 ![image](https://user-images.githubusercontent.com/111422800/196079364-9a182859-00c5-4c7e-8847-9cfcdbd28f28.png)


<h2>要求四：SQL Aggregate Functions</h2>

1.　取得 member 資料表中，總共有幾筆資料 ( 幾位會員 )。</br>

    SELECT COUNT(*) FROM member;

![image](https://user-images.githubusercontent.com/111422800/196085326-08f1c037-7b96-4da4-9883-1d3e81c2f8ed.png)

    
2.　取得 member 資料表中，所有會員 follower_count 欄位的總和。</br>

    SELECT SUM(follower_count)	FROM member;

![image](https://user-images.githubusercontent.com/111422800/196085969-18ec8b3d-9db0-4f95-ac32-ed3d84db47fe.png)


3.　取得 member 資料表中，所有會員 follower_count 欄位的平均數。</br>

    SELECT AVG(follower_count)	FROM member;
    
![image](https://user-images.githubusercontent.com/111422800/196086214-38f71363-2e31-4ce5-9b15-8cf5032912c5.png)


<h2>要求五：SQL JOIN (Optional)</h2>

1.　建立message資料表紀錄留⾔資訊。</br>

      CREATE TABLE message(
        id BIGINT PRIMARY KEY AUTO_INCREMENT,
        member_id BIGINT NOT NULL,
        content  VARCHAR(255) NOT NULL,
        like_count INT UNSIGNED  NOT NULL DEFAULT 0,
        time  DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP()
      );

  　   member_id外鍵對應 member 資料表中的 id
      
      ALTER TABLE message ADD FOREIGN KEY (member_id) REFERENCES member(id);
      
![image](https://user-images.githubusercontent.com/111422800/196088344-a2794ee7-7921-4c0a-8b31-47f2d34b83ce.png)

   插入message資料

      INSERT INTO message(id,member_id,content,like_count,time) VALUES(1,2,"星期六有空嗎",98,"2022-10-01 08:00:00");

      INSERT INTO message(member_id,content,like_count) VALUES(2,"什麼時候開學?",6);

      INSERT INTO message(member_id,content,like_count,time) VALUES(3,"迪士尼好玩嗎?",5,"2022-09-01 09:00:00");

      INSERT INTO message(member_id,content,like_count,time) VALUES(4,"萬聖節要不要去環球影城?",66,"2022-10-01 23:00:00");

      INSERT INTO message(member_id,content,like_count) VALUES(5,"迪士尼好玩嗎?",98);  
      

![image](https://user-images.githubusercontent.com/111422800/196092244-2339d451-96bb-47bd-9376-105e490d0781.png)


2.　使⽤ SELECT 搭配 JOIN 語法，取得所有留⾔，結果須包含留⾔者會員的姓名。</br>
    
    SELECT member.name,message.content FROM member INNER JOIN message ON member.id =message.member_id;
 
 ![image](https://user-images.githubusercontent.com/111422800/196095195-6cc39e2b-da38-4b1d-9995-b61e31a4aacc.png)


3.　使⽤ SELECT 搭配 JOIN 語法，取得 member 資料表中欄位 username 是 test 的所有留⾔，資料中須包含留⾔者會員的姓名。</br>
    
    INSERT INTO message(member_id,content) VALUES(1,"test沒留言，幫他加一筆留言");
    INSERT INTO message(member_id,content) VALUES(1,"再幫test加一筆留言");

    SELECT member.username, member.name, message.content FROM member
    INNER JOIN message ON member.id =message.member_id WHERE member.username = "test" ;
    
![image](https://user-images.githubusercontent.com/111422800/196097128-70fc3770-d8bd-4f40-b052-3d2b557fcf51.png)


4.　使⽤ SELECT、SQL Aggregate Functions 搭配 JOIN 語法，取得 member 資料表中欄位 username 是 test 的所有留⾔平均按讚數。</br>
    
   因為剛剛把message第7第8筆id(username 是 test )的資料都沒給他案讚數，這樣平均起來還是會0，所以為了讓他想測試平均，
   我這邊先修改一下第7第8筆id的按讚數。
    
    UPDATE message SET like_count=10 WHERE id=7;
    UPDATE message SET like_count=8 WHERE id=8;
    
![image](https://user-images.githubusercontent.com/111422800/196098855-33ee432a-6c59-4b95-b43c-19c62872493b.png)

    
    SELECT AVG(like_count), member.username FROM member 
    INNER JOIN message ON member.id =message.member_id WHERE member.username = "test" ;

![image](https://user-images.githubusercontent.com/111422800/196099766-a54e37d6-5c3f-48d3-aa23-d96a6e5d7f93.png)

    
   

