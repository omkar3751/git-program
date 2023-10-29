# using for loop print thr character help to ASCII value

for i in range(65,71):
    for j in range(65,i+1):
        print(chr(j), end=" ")
    print()
Output:
          A 
          A  B 
          A  B  C 
          A  B  C  D 
          A  B  C  D  E 
          A  B  C  D  E  F 


for i in range(70,63,-1):
    for j in range(i+1,64,-1):
        print(chr(j), end=" ")       # Reverse order
    print()
Output:
        G  F  E  D  C  B  A 
        F  E  D  C  B  A 
        E  D  C  B  A 
        D  C  B  A 
        C  B  A 
        B  A 
        A 


for i in range(64,71):
    for j in range(i+1,64,-1):
        print(chr(j), end=" ")                   # Descending order
    print()
Output:
          A 
          B  A 
          C  B  A 
          D  C  B  A 
          E  D  C  B  A 
          F  E  D  C  B  A 
          G  F  E  D  C  B  A
        ​
