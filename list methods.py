# list methods :

1.list.append()          # input the single value in last index
2.list.extend()          # input the multiple value in last index
3.list.pop()             # onetime show and permanantly delete the value
4.list.sort()            # sort by ascending order

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

lst.sort()                                                 # defaultly ascending order
Output:
        ['css','javascript','php','python','xml']
