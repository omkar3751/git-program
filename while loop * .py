# create a * pattern program
# 1.
i = 1
while i < = 6:
  print(i * '*')
  i = i + 1
Output:
        *
        * *
        * * *
        * * * *
        * * * * *
        * * * * * *
# 2.
i = 1
while i < = 6:
  print(i * '*')
  i = i - 1

if i == 0:
  break
Output:
        * * * * *
        * * * *
        * * *
        * *
        *
