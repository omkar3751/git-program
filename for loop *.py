# print the * pattern 
1.
for i in range(1,5+1):
    print(i * "*")

Output:
        *
        * *
        * * *
        * * * *
        * * * * *
          
2.
for i in range(5,0,-1):
    print(i * "*")

Output:
        * * * * *
        * * * *
        * * *
        * *
        *
3.
n=5
for i in range(n):
    for j in range(i+1):
        print(' ',end=' ')
    for k in range(i,n):
        print('*',end=' ')
    print()
Output:
         * * * * * 
           * * * * 
             * * * 
               * * 
                 * 
4.
n=5
for i in range(n):
    for j in range(n):
        print('*',end=' ')
    print()
Output:
        *  *  *  *  * 
        *  *  *  *  * 
        *  *  *  *  * 
        *  *  *  *  * 
        *  *  *  *  * 
5.
n=5
for i in range(n):
    for j in range(i,n):
        print(' ',end=' ')
    for k in range(i):
        print('*',end=' ')
    for j in range(i+1):
        print('*',end=' ')
    print()
Output:
          * 
        * * * 
      * * * * * 
    * * * * * * * 
  * * * * * * * * * 
5.
n=5
for i in range(n):
    for j in range(i+1):
        print(' ',end=' ')
    for l in range(i,n-1):
        print('*',end=' ')
    for k in range(i,n):
        print('*',end=' ')
    print()
Output:
      * * * * * * * * * 
        * * * * * * * 
          * * * * * 
            * * * 
              * 
7.
n=5
for i in range(n-1):
    for j in range(i,n):
        print(' ',end=' ')
    for j in range(i):
        print('*',end=' ')
    for j in range(i+1):
        print('*',end=' ')
    print()
for i in range(n):
    for j in range(i+1):
        print(' ',end=' ')
    for j in range(i,n-1):
         print('*',end=' ')
    for j in range(i,n):
         print('*',end=' ')
    print()
Output:
          * 
        * * * 
      * * * * * 
    * * * * * * * 
  * * * * * * * * * 
    * * * * * * * 
      * * * * * 
        * * * 
          * 
