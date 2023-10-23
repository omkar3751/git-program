# list methods :

1.list.append()          # input the single value in last index
2.list.extend()          # input the multiple value in last index
3.list.pop()             # onetime show and permanantly delete the value
4.list.sort()            # sort by ascending order
5.list.remove()          # remove the particular value
6.list.count()           # number of time thats occurence 
7.list.index()           # find the index number

lst=['python','html','css']                                

lst.append('java')                                        # pass the single argument
Output:
        ['python','html','css','java']

lst.extend(['php','xml','javascript'])                    # pass the multiple argument
Output:
        ['python','html','css','php','xml','javascript']

lst.pop(1)                                                # pass the index number
Output:
        ['python','css','php','xml','javascript']

lst.sort()                                                # defaultly ascending order
Output:
        ['css','javascript','php','python','xml']

lst.remove('xml')                                          # pass the argument
Output:
        ['css','javascript','php','python']

lst=[1,2,3,4,5,6,,2,7,8,2,9]
lst.count(2)                                               # pass the argument
Output:
        3

lst.index('css')                                           # pass the argument
Output:
        2
