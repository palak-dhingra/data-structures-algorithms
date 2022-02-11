def main():
    # Print all prime numbers less than or equal to N

    n = int(input("enter n - "))
    print(n)

    list_of_prime = [True for i in range(n+1)];
    for i in range(2, n+1):
        if(list_of_prime[2]):
            for j in range(i*2, n+1, i):
                list_of_prime[j] = False
            
    
    for i in range(2, n+1):
        if(list_of_prime[i]):
            print(i, end=" ");
    
if __name__ == "__main__":
    main()

