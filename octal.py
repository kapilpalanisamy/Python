'''' #decimal to octal
def func(num):
    oct=0
    power=1
    while num!=0:
        digit=num%8
        oct=digit*power + oct
        power *=10
        num =num //8
    return oct
    '''

#octal to decimal
def func(num):
    digit=0
    oct_power=1
    dec=0
    while num!=0:
        digit=num%10
        dec=dec+digit*oct_power
        oct_power *=8
        num //=10
    return dec 
if __name__=="__main__":
    num=int(input())
    sol=func(num)
    print(sol)
    
