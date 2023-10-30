# Built-in functions.
1.abs()              # To return the Positive value absolute function
2.all()              # To return the True or False value
3.divmod()           # To return the division or modulous
4.enumerate()        # To return the index wise element
5.filter()           # Do not return negative value
6.isinstance()       # list or tuple,set ,dict
7.map()              # loop wise execute 
8.reduce()           # Directly print the code

1.
a = -4.4566
print(abs(a))
Output:
        4.4566
2.
lst=[0,1,2,3,4,5]         # 0 preset in list then return the false
print(all(lst))
Output:
        False
3.
print(divmod(13,9))
Output:
        (1,4)
4.
lst=[1,2,3,4,5]
for i in enumerate(lst):
  print(i)
Output:
        (0, 1)
        (1, 2)
        (2, 3)
        (3, 4)
        (4, 5)
5.
lst = range(-20,20)
positive_num = list(filter(positive_num))
Output:
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
6.
a = [1,2,3,4,5,6,7]
print(isinstance(a,list))
Output:
        True
7.
def power_3(n):
    return n**3                
lst=[1,2,3,4,5]
d=list(map(power_3,lst))
print(d)
Output:
        [1, 8, 27, 64, 125]
8.
lst=[1,2,3,4]
from functools import reduce          # import the library functool in reduce function
def mul(x,y):
    prod = x * y
    return prod
f=reduce(mul,lst)
print(f)
Output:
        24
