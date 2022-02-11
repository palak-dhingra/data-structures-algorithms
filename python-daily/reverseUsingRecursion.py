def reverseRec(inputStr, n):
  if n==-1:
    return
  print(inputStr[n], end = " ");
  reverseRec(inputStr, n-1)
  


  

def main():
    inputStr = "pulkit"
    reverseRec(inputStr, len(inputStr)-1)

if __name__ == "__main__":
    main()

