for i in range (1,1001):
    first=i//100
    div=i%100
    mid=div//10
    last=i%10
    if(first==mid) or (first==last) or (first==last==mid):
        print(i)