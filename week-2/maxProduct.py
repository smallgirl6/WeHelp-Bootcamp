def maxProduct(nums):
    count = [i for i in nums if i<0]  #看看數列nums有幾個負數
        
    for i in nums:
        maxnum1 = max(nums)
        nums.remove(maxnum1)

        for i in nums:
            maxnum2 = max(nums)
            break
        break
    result1 = maxnum1 * maxnum2  #若是數列nums只有一個負數或沒有負數，那就可以直接找最大的正數了

    if len(count)>1:                  #若是數列nums有兩個以上的負數，那要考慮負負得正的問題
        
        for i in count:
            maxnum3 = min(count)  #數列中最小的兩個負值相乘所得的積會是所有數列負值中最大的積，所以取最小
            count.remove(maxnum3)
            for i in count:
                maxnum4 = min(count)
                break
            break
        result2 = maxnum3 * maxnum4
    else:
        result2 = result1 #若是數列nums只有一個負數或沒有負數，那就把result1帶到result2，因為我只想要result1的值，

    
    
    if  result1>result2: #比較數列nums只有一個負數或沒有負數的結果 和 數列nums有兩個以上的負數的結果誰大
        return result1
    else:
        return result2

                    

print(maxProduct([5, 20, 2, 6]) )
print(maxProduct([10, -20, 0, 3]) )
print(maxProduct([10, -20, 0, -3]))
print(maxProduct([-1, 2]) )
print(maxProduct([-1, 0, 2]))
print(maxProduct([5,-1, -2, 0]))
print(maxProduct([-5, -2]))






