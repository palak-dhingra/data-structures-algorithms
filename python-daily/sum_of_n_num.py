def sumOfNNumber(n):
  if n==0:
    return 0;
  return n + sumOfNNumber(n-1)
if __name__=="__main__":
  n = int(input("enter value of n - "))
  if(n<0):
    print("invalid number")
  else:
    result = sumOfNNumber(n)
    print("sum of", n, "natural number - ", result)