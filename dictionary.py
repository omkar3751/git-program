# Dictionary is key & value pairs

dic = {'Name':['omkar','akshay','kumar'],'age':{1:21,2:23,3:24}}
print(dic)
Output:
        {'Name': ['omkar', 'akshay', 'kumar'], 'age': {1: 21, 2: 23, 3: 24}}


print(dic.keys())
Output:
        dict_keys(['Name', 'age'])

print(dic.values())
Output:
        dict_values([['omkar', 'akshay', 'kumar'], {1: 21, 2: 23, 3: 24}])

print(dic.items())                       # to return the all items 
Output:
        dict_items([('Name', ['omkar', 'akshay', 'kumar']), ('age', {1: 21, 2: 23, 3: 24})])

print(dic.get('Name'))                    # get the specific key values
Output:
        ['omkar', 'akshay', 'kumar']

print(dic.get('age'))
Output:
        {1: 21, 2: 23, 3: 24}
