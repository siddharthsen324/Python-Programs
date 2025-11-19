a,b,c,d=map(int,input().split())
x=(a%100)*(b%100)
y=x%100
z=(y*(c%100))%100
s=(z*(d%100))%100
print("{:02d}".format(s))
