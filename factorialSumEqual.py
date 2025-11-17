'''jisne factorial ke sum ke equal ho eg 145=1!+4!+5!'''
for i in range(1,1000000):
    sum = 0
    t1 =i
    while(t1>0): 
        t=t1%10
        fact = 1
        for j in range(1,t+1):
            fact = fact * j
        sum = sum + fact
        t1 = t1//10
    if sum == i:
        print(i)

    