a,b,c,d,e=input().split()
a=int(a)
b=(b)
c=int(c)
d=(d)
e=int(e)
if b=='+':
    if a+c==e:
        print("Yes")
    else:
        print(a+b)
if b=='-':
    if a-c==e:
        print("Yes")
    else:
        print(a-c)
if b=='*':
    if a*c==e:
        print("Yes")
    else:
        print(a*c)
if b=='/':
    if a/c==e:
        print("Yes")
    else:
        print(a/c)