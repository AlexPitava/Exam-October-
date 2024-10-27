def eureka(a,b):
    lst = []
    
    for num in range(a, b + 1):
        eureka_sum = sum(int(num)) ** (i + 1), i in enumerate(num)
        if eureka_sum == num:
            lst.append(num)
    
    return lst

print(eureka(100, 1000))