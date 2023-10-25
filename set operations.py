# set operations
# take a two sets & apply the operations

1.union()                  [|]   # combine a two sets not in common value is one time print
2.intersection()           [&]   # Return the Common value
3.difference               [-]   # different value print another set
4.symmetric_difference()   [^]   # return the two cobine set but not common value

a = {1,2,3,4,5}
b = {4,5,6,7,8}

a.union(b)
Output:
        {1,2,3,4,5,6,7,8}

a.intersection(b)
Output:
       {4,5}

a.difference(b)
Output:
        {1,2,3}
b.difference(a)
Output:
        {6,7,8}

a.symmetric_difference(b)
Output:
        {1,2,3,6,7,8}
