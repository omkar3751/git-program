# find the hcf using def function

def computehcf(a,b):
    smaller = a if a < b else b
    hcf = 1
    for i in range(1,smaller+1):
        print(i)
        if(a % i == 0) and (b % i == 0):
            hcf = i
    return hcf
  
num1 = 26
num2 = 3

print("HCF of {0}and {1} is:{2}".format(num1,num2,computehcf(num1,num2)))

Output:

        1
        2
        3
        HCF of 26 and 3 is:1
