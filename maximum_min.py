x,y,z =map(int,(input().split()))

if x<y and x<z:
    print(x,end=" ")
elif y<z:
    print(y,end=" ")
else:
    print(z,end=" ")
if x>y and x>z:
    print(x,end="")
elif y>z:
    print(y,end="")
else:
    print(z,end="")    