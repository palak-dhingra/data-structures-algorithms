def dec(n):
  if n==0:
    return
  print(n)
  dec(n-1)
  

def main():
    n = 7
    dec(n);
if __name__ == "__main__":
    main()

