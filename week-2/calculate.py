
def calculate(min, max, step):
    result=0
    if (max-min)%step==0:          
        for i in range(min,max+step,step): 
            result += i 
        return result
    else:
        for i in range(min,max,step): 
            result += i 
        return result


print(calculate(1, 3, 1))
print(calculate(4, 8, 2))
print(calculate(-1, 2, 2))






# result=0
# for i in range(4,8,2): 
#     result += i     
# print(result)



