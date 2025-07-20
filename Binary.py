'''#decimal to binary
def func(num):
    oct=0
    power=1
    while num!=0:
        digit=num%2
        oct=digit*power + oct
        power *=10
        num =num //2
    return oct
    '''

#binary to decimal
def func(num):
    digit=0
    oct_power=1
    dec=0
    while num!=0:
        digit=num%10
        dec=dec+digit*oct_power
        oct_power *=2
        num //=10
    return dec 
if __name__=="__main__":
    num=int(input())
    sol=func(num)
    print(sol)
    
