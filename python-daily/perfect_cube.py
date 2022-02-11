def main():
    # Perfect Cube
    n = int(input("n - "));
    print(n)
    v = round(pow(n,1/3))
    if(pow(v,3) == n):
        print("it's a cube")
    else:
        print("not a cube")


   
    
if __name__ == "__main__":
    main()

