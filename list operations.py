# list operations 
lst = [1,2,3,4,5,6,7]

print(len(lst))
Output :
        6

lst.append(4)
Output:
        [1,2,3,4,5,6,7,4]

print(lst.count(4)) # How many 4 are on the list 'lst'
Output:
        2

print(lst.index(2)) # What is the index of the number 2 in the list 'lst'
Output:
        1

lst.insert(8, 9) # Add number 9 to the index 8.
print(lst)
Output:
        [1,2,3,4,5,6,7,4,9]

print(max(lst)) # What is the maximum number in the list
Output:
        9

print(min(lst)) # What is the minimum number in the list
Output:
        1

print(sum(lst)) # What is the sum of the numbers in the list
Output:
        41
