#765387834
#753736884
def odd_even(num):
    oddset=0
    evenset=0
    oddpower=1
    evenpower=1
    while num!=0:
        digit=num%10
        if digit%2==0:
            evenset=digit*evenpower+evenset
            evenpower*=10
        else:
            oddset=digit*oddpower+oddset
            oddpower *=10
        num = num//10
    return oddset*evenpower +evenset
if __name__=="__main__":
    num=int(input())
    sol=odd_even(num)
    print(sol)