
# sum_10 = [] 

# for x in range(1, 1001):
#     total = 0
    
#     for digit in str(x): 
#         total = total + int(digit)  
    
#     if total == 10: 
#         sum_10.append(x)  

# print(sum_10)


''' given number 1 to 500 ,print numbers which on squaring the squared number should have same number in the last of the same number '''
# temp1 = []
# temp2 = []
# temp3 = []
# for i in range(1 ,11) :
#     if i <=10 :
#         sqr = i**2 #25
#         lst = sqr % 10 # 5
#         if lst == i :
#             temp1.append(i)
    
# for j in range(11 , 101) :
#     sqr2 = j**2 
#     lst2 = sqr2 % 100
#     if lst2 == j :
#         temp2.append(j)
    
# for x in range(101 , 1001) :
#     sqr3 = x**2 
#     lst3 = sqr3 % 1000
#     if lst3 == x :
#         temp3.append(x)


# print(temp1+temp2+temp3)


''' efficient logic for same question'''

# temp = []

# for i in range(1, 1001):

#     square = i**2

#     digits = len(str(i))  
#     last_digits = square % (10 ** digits)

    
#     if last_digits == i:
#         temp.append(i) 


# print(temp)


'''let number is given 1 to 200 , we have to print numbers which has only 4 factors'''


# num = []

# for i in range(2 , 201) :
#     fact = []
#     for j in range( 1, i-1) :
#         if i % j == 0 :
#             fact.append(j)
#     if len(fact) == 4 :
#         num.append(i)
    
# print(num)

''' Correct logic is this : '''
# num = []

# for i in range(2, 201):
#     count = 0
#     for j in range(1, i+1):  # include the number itself
#         if i % j == 0:
#             count += 1
#     if count == 4:
#         num.append(i)

# print(num)


'''given a number between 100 to 1000 , we have to do sum of first and last digit and print the number which should be the middle number  '''


# num = []
# for i in range(100 , 1000) :
#     first_dgt = int(str(i)[0])
#     last_dgt = i % 10
#     mid_dgt = int(str(i)[1])
#     if (first_dgt + last_dgt) == mid_dgt :
#         num.append(i)
# print(num)


'''given number from 100 to 1000 and print numbers which are divisible by their reverse numbers'''

num = []
for i in range(100 , 1000) :
    reverse = int(str(i)[: : -1])
    if i % reverse == 0 :
        num.append(i)
print(num)
    



