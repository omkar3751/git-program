# User input value & find even or odd 

a=[]                
even=[]
odd=[]
n=int(input("Enter the length of list"))
for i in range(1,n+1):
        num=(int(input("Enter the numbers:")))
        a.append(num)
        if i % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
print(f'Original list is: {a}')
print(f'Even list is: {even}')
print(f'Odd list is: {odd}')
