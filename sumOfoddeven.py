

for i in range(100,1001):
    first_dgt=int(str(i)[0])
    last_dgt=i%10
    mid_dgt=int(str(i)[1])
    if (first_dgt+last_dgt+mid_dgt)%2==0:
        print(i)
        

