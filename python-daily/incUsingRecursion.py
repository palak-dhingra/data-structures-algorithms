def inc(n):
  if n==0:
    return
  
  inc(n-1)
  print(n)

def main():
    n = 7
    inc(n);
if __name__ == "__main__":
    main()

