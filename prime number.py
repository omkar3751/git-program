# 1. Print the prime numbers

lower_value=int(input("Enter the lower limit: "))
upper_value=int(input("Enter the upper limit: "))

for number in range(lower_value,upper_value+1):
    if number > 1:
        for i in range(2,number):
            if number % i == 0:
                break
        else:
            print(number)

Output:
        Enter the lower limit: 5
        Enter the upper limit: 20
        5
        7
        11
        13
        17
        19
# 2. number of element in the list

num=int(input("Enter the number of element: "))

lst=[]
prime=[]

for i in range(1,num+1):
    val=int(input("Enter value: "))                         
    lst.append(val)
    if val > 1:
        for i in range(2,val):
            if val % i ==0:
                break
        else:
            prime.append(val)
print(prime)

Output:
        Enter the number of element: 3
        Enter value: 4
        Enter value: 7
        Enter value: 11
        [7, 11]
