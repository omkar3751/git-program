# elment is even or odd in list append method

lst=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
even=[]
odd=[]

for i in lst:
  if i % 2 == 0:
    even.append(i)
  else:
    odd.append(i)
print(even)
print(odd)

Output:
        even=[2,4,6,8,10,12,14,16,18,20]
        odd=[1,3,5,7,9,11,13,15,17,19]
