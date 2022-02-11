def pow(n, p):
  if p==0:
    return 1
  return n * pow(n, p-1)

def main():
    n = 2
    p = 10
    print(pow(n, p))
if __name__ == "__main__":
    main()

