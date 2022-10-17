
CREATE DATABASE `website`;
USE `website`;

-- 要求2：建立資料庫和資料表
CREATE TABLE member(
	id BIGINT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    follower_count INT UNSIGNED  NOT NULL DEFAULT 0,
    time  DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP()
    
);

-- 要求三：SQL CRUD
INSERT INTO member(id,name,username,password,follower_count,time) VALUES(1,"Jerry","test","test",90,"2022-08-30 08:00:00");
INSERT INTO member(name,username,password,follower_count,time) VALUES("Ken","Ken001","cc121",100,"2022-08-25 06:00:00");
INSERT INTO member(name,username,password,follower_count,time) VALUES("Sun","Sun001","bb221",99,"2022-09-28 15:00:00");
INSERT INTO member(name,username,password,follower_count,time) VALUES("Benny","Benny001","ac131",200,"2022-10-15 23:00:00");
INSERT INTO member(name,username,password) VALUES("Lucca","Lucca001","cc121");

SELECT * FROM member ORDER BY time desc;
SELECT * FROM member ORDER BY time desc LIMIT 1,3;
SELECT * FROM member WHERE username="test" ;
SELECT * FROM member WHERE username="test" && password="test" ;

SET SQL_SAFE_UPDATES = 0;
UPDATE member SET name="test2" WHERE username="test";
SELECT * FROM member;

-- 要求四：SQL Aggregate Functions
SELECT COUNT(*) FROM member;
SELECT SUM(follower_count)	FROM member;
SELECT AVG(follower_count)	FROM member;

-- 要求五：SQL JOIN (Optional)
CREATE TABLE message(
	id BIGINT PRIMARY KEY AUTO_INCREMENT,
    member_id BIGINT NOT NULL,
    content  VARCHAR(255) NOT NULL,
    like_count INT UNSIGNED  NOT NULL DEFAULT 0,
    time  DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP()
    
);
SELECT * FROM message;
ALTER TABLE message ADD FOREIGN KEY (member_id) REFERENCES member(id);


INSERT INTO message(id,member_id,content,like_count,time) VALUES(1,2,"星期六有空嗎",98,"2022-10-01 08:00:00");
INSERT INTO message(member_id,content,like_count) VALUES(2,"什麼時候開學?",6);
INSERT INTO message(member_id,content,like_count,time) VALUES(3,"迪士尼好玩嗎?",5,"2022-09-01 09:00:00");
INSERT INTO message(member_id,content,like_count,time) VALUES(4,"萬聖節要不要去環球影城?",66,"2022-10-01 23:00:00");
INSERT INTO message(member_id,content,like_count) VALUES(5,"迪士尼好玩嗎?",98);

-- DELETE FROM message WHERE id=6;

SELECT member.name,message.content FROM member 
INNER JOIN message ON member.id =message.member_id;

INSERT INTO message(member_id,content) VALUES(1,"test沒留言，幫他加一筆留言");
INSERT INTO message(member_id,content) VALUES(1,"再幫test加一筆留言");

SELECT member.username, member.name, message.content FROM member 
INNER JOIN message ON member.id =message.member_id WHERE member.username = "test" ;

UPDATE message SET like_count=10 WHERE id=7;
UPDATE message SET like_count=8 WHERE id=8;

SELECT AVG(like_count), member.username FROM member 
INNER JOIN message ON member.id =message.member_id WHERE member.username = "test" ;