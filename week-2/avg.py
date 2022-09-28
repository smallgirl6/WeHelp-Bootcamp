def avg(data):
    sum=0
    for i in data["employees"]: #查看employees的value(串列)
        for k,v in  i.items():  #查看每個value(串列)內的每個字典的key 和value
            if k=="manager" and v==False: #找出不是manager的人
                notmanager=len(i)          #不是manager的人數有幾人
                sum =sum +(i.get("salary")) #抓出不是manager的人的薪資，並把它放入sum 
    avg = sum/notmanager             #算平均
    print(avg)


avg({
    "employees":[
        {
        "name":"John",
        "salary":30000,
        "manager":False
        },
        {
        "name":"Bob",
        "salary":60000,
        "manager":True
        },
        {
        "name":"Jenny",
        "salary":50000,
        "manager":False
        },
        {
        "name":"Tony",
        "salary":40000,
        "manager":False
        }
    ]
}) # 呼叫 avg 函式

