def twoSum(nums, target):
    for i in range(0,len(nums)): #第一隻指針從0開始遍遍歷到最後
        for j in range(1,len(nums)): #第二隻指針從1開始遍歷到最後
            if (nums[i]+nums[j]==target) and (i!=j): #如果指針指的位置的值加起來等於target 且 不是指在同個位置(不是同一個值)
                return [i,j] #傳回指針的位置
result=twoSum([2, 11, 7, 15], 9)
print(result) # show [0, 2] because nums[0]+nums[2] is 9
