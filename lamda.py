# double = lambda x: x*2

# print(double(5))
# Example use with filter()
# lst = [1, 2, 3, 4, 5]
# even_lst = list(filter(lambda x: (x%2 == 0), lst))#filter only true value return karta hai .
# print(even_lst) 
lst = [1,2,3,4,5]
new_lst = list(map(lambda x: x ** 2 , lst))
print(new_lst)