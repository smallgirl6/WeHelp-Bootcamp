
def func(a):
    def smallfunc(b,c):
        bc=b*c
        abc = a+bc
        return abc   #print(abc)
    return smallfunc
    
    
print(func(2)(3, 4))
print(func(5)(1, -5))
print(func(-3)(2, 9))
