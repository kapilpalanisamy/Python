def func(num):
    power = 1
    while num//power > 9:
        power *= 10

    while power != 0:
        digit = num // power
        print(digit)
        num %= power
        power //= 10

if __name__ == "__main__":
    num = int(input())
    func(num)