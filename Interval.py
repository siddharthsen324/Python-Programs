x=input()
x=float(x)
if x<0 or x>100:
    print("Out of Intervals")
elif 0<=x<=25:
    print("Interval [0,25]")
elif 25<x<=50:
    print("Interval (25,50]")
elif 50<x<=75:
    print("Interval (50,75]")
elif 75<x<=100:
    print("Interval (75,100]")
