def towerOfHanoi(n, src, helper, dest):
  if(n==1):
    print("moving disc", n, "from", src, "to", dest)
    return

  towerOfHanoi(n-1, src, dest, helper)
  print("moving disc", n, "from", src, "to", dest)
  towerOfHanoi(n-1, helper, src, dest)
if __name__=="__main__":
  n = int(input("enter value of n - "))
  if(n<0):
    print("invalid number")
  else:
    towerOfHanoi(n, 'S', 'H', 'D')