import math
x,y=input().split()
x=int(x)
y=int(y)
a=math.floor(x/y)
b=math.ceil(x/y)

print(f"floor {x} / {y} = {a}")
print(f"ceil {x} / {y} = {b}")
print( "round {} / {} =".format(x,y).format(x,y), int(x/y + 0.5) if x/y > 0 else int(x/y-0.5))