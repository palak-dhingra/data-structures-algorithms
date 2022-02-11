def printFibSequence(a, b, n):
  if n==0:
    return;
  c = a+b
  print(c)
  printFibSequence(b, c, n-1)
if __name__=="__main__":
  n = int(input("enter value of n - "))
  if(n<0):
    print("invalid number")
  else:
    a = 0
    b = 1
    print(a)
    print(b)
    printFibSequence(a, b, n-2)