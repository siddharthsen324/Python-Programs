n=int(input())
o=0
e=0
n1=n
cout=1
while(n1>0):
    t=n1%10
    if(cout%2==0):
        e=e+t
    else:
        o=o+t
    cout+=1
    n1=n1//10
if n>99:
    print("the odd sum:",o)
    print("the even sum :",e)
else:
    print("the odd sum:",e)
    print("the even sum :",o)

