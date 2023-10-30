# variable i.e a and b in hcf should be multiple of 5 only

def computehcf(a,b):
    smaller = a if a < b else b
    hcf = 1
    for i in range(1,smaller + 1):
        print(i)
        if(a % i == 0) and (b % i == 0):
            hcf = i
    return hcf
def mult_5(a,b):
    if(a % 5 == 0) and (b % 5 == 0):
        hcf_5 = computehcf(a,b)
        return(f'HCF of {a} & {b} is {hcf_5}')
    elif(a % 5 == 0) or (b % 5 == 0):
        hcf_5=computehcf(a,b)
        return(f'HCF is {hcf_5} but one of the is not multiple of 5')
    else:
        return(f'Neither {a} nor {b} is multiple of 5')
num1=int(input("enter the number"))
num2=int(input("enter the number"))
print(f'{mult_5(num1,num2)}')

Output:
        enter the number 15
        enter the number 25
        1
        2
        3
        4
        5
        6
        7
        8
        9
        10
        11
        12
        13
        14
        15
        HCF of 15 & 25 is 5
