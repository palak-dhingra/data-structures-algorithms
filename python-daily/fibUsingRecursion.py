def fib(n):
  if n==1 or n==0:
    return n
  return fib(n-1) + fib(n-2)

def main():
    n = 6
    print(fib(n))
if __name__ == "__main__":
    main()

