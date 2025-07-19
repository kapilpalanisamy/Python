def is_prime(num):
    if num < 2:
        return False
    if num == 2 or num == 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    
    cf = 5
    while cf * cf <= num:
        if num % cf == 0 or num % (cf + 2) == 0:
            return False
        cf += 6
    
    return True

def main():
    num = int(input("Enter a number: "))
    if is_prime(num):
        print("P R I M E")
    else:
        print("Not Prime")
if __name__ == "__main__":
    main()
    