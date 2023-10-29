# create table with while loop

num = int(input("Enter the number :"))
i = 1

while i <=10:                                          while i <=10:
  print(num * i)                                          print(f'{num} * {i} = {num*i}')
  i = i+1                                                 i = i+1

Output:                                                Output:
        Enter the number: 3                                    Enter the number: 3

        3                                                       3 * 1 = 3                                             
        6                                                       3 * 2 = 6
        9                                                       3 * 3 = 9
        12                                                      3 * 4 = 12 
        15                                                      3 * 5 = 15
        18                                                      3 * 6 = 18
        21                                                      3 * 7 = 21
        24                                                      3 * 8 = 24
        27                                                      3 * 9 = 27
        30                                                     3 * 10 = 30
