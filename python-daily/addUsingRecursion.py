def add(n):
  if n==0:
    return n
  return n + add(n-1)

def main():
    n = 6
    print(add(n))
if __name__ == "__main__":
    main()

