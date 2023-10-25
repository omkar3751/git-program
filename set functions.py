# set functions

1.set.add()                      # add the element i last index
2.set.update()                   # To add the multiple values
3.set.remove()                   # To remove 


set1= {1,(2,3,4),5}

set1.add('Data')

print(set1)
Output:
        {(2,3,4),1,2,'Data'}

set1.update('science',2,3+5j,True)

print(set1)
Output:
        {(2,3,4),1,2,'science',True,2+3j}

set1.remove('science')

print(set1)
Output:
        {92,3,4),1,2,True,2+3j}
