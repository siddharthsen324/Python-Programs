a = input().replace(" ", "")
left, right = a.split('=')   
right = int(right)
if '+' in left:
    c,d = left.split('+')
    if int(c) + int(d) == right:
        print("Yes")
    else:
        print(int(c) + int(d))    
elif '-' in left:
    c,d = left.split('-')
    if int(c) - int(d) == right:
        print("Yes")
    else:
        print(int(c) - int(d))    
else:
    c,d = left.split('*')
    if int(c) * int(d) == right:
        print("Yes")
    else:
        print(int(c) * int(d))