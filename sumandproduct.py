

for i in range(1,1001):
    first_dgt=int(str(i)[0])
    last_dgt=i%10
    mid_dgt=int(str(i)[1])
    product=first_dgt*last_dgt*mid_dgt
    sum=first_dgt+last_dgt+mid_dgt
    if product==sum :
     print(i)