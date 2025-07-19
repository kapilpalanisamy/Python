def func(num):
    sum=0
    while num !=0:
        digit = num % 10
        print(digit)
        sum += digit
        num //=10
    print('Sum',sum)
if __name__ == "__main__":
    num=int(input())
    sol=func(num)