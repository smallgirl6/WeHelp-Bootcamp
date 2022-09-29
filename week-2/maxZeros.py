

def maxZeros(nums):
    zero = 0 #計算連續出現0的次數
    maxZero = 0  #計算續出現0的最大次數
    for num in nums:#遍歷nums
        if num == 0: #若元素 == 0:
            zero +=1  #計算zero的總和地方加上1次
            maxZero = max(maxZero,zero)   #第一次出現的zero值會放到maxZero，隨後若出現的zero若比maxZero大，就會取代舊maxZero
        else:
            zero = 0 #若沒有出現0，那計算zero的總和就是0次了
    print(maxZero)

maxZeros([0, 1, 0, 0]) # 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]) # 得到 4
maxZeros([1, 1, 1, 1, 1]) # 得到 0
maxZeros([0, 0, 0, 1, 1]) # 得到 3