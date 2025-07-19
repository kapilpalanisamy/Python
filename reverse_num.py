# this method cant be used when we have trailing zeros.
def func(num):
    rev_num=0
    while num !=0:
        digit = num % 10
        rev_num = rev_num * 10 + digit
        num = num // 10
    return rev_num
if __name__ == "__main__":
    num=int(input())
    sol=func(num)
    print(sol)
