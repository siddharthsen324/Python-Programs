s=input()
if '<' in s:
    a,b=s.split('<')
    a=int(a)
    b=int(b)
    if a<b:
        print("Right")
    else:
        print("Wrong")
elif '>' in s:
    a,b=s.split('>')
    a=int(a)
    b=int(b)
    if a>b:
        print("Right")
    else:
        print("Wrong")
elif '=' in s:    
    a,b=s.split('=')
    a=int(a)
    b=int(b)
    if a==b:
        print("Right")
    else:
        print("Wrong")    
