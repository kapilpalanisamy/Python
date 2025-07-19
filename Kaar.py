def Kaar(n,a,m):
    #n=a*m + d
    #d=n - (a*m)
    d = n - (a*m)
    if d>0 and m%d==0:
        return m,d

def main():
    n=int(input())
    a=int(input())
    results = [] 
    sum=0
    for m in range(1,(n//a)+1):
        result = Kaar(n, a, m)
        if result:
            results.append(result)
            sum += result[0]
    print(results)
    print("Sum:", sum)
    
if __name__ == "__main__":
    main()