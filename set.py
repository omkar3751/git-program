# Set is one of in data types in Python used to store of data including List, Tuple, and Dictionary.
# A set itself may be modified,it is an immutable type.
# You can denote a set with a pair of curly brackets {}

empty_set=set()

print(empty_set)
Output:
        set()

lst=[1,2,3,4,5,6,7,8,3,2,1,6,8,9]

set1=set(lst)
print(set1)
Output:
        {1,2,3,4,5,6,7,8,3,2,1,6,8,9}

set1=tuple(lst)
print(set1)
Output:
        (1,2,3,4,5,6,7,8,3,2,1,6,8,9)
