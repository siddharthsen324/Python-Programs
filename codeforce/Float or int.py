x=input()
if '.' in x:
    part=x.split('.')
    if part[1]=="000" or part[1]=="0" or part[1]=="00":
     print("int",part[0])
    else:
       print("float",part[0],"0."+part[1])

else:
   print("int",x)