count = 0

for i in range(100,1001):
    first_dgt=int(str(i)[0])
    last_dgt=i%10
    mid_dgt=int(str(i)[1])
    if(first_dgt==mid_dgt) or (first_dgt==last_dgt) or (first_dgt==last_dgt==mid_dgt):
        print(i)
        count= count+1

print(" number of digit" , count)