def replacePi(inputStr):
  if(len(inputStr)==0):
    return;

  if inputStr[0]=="p" and len(inputStr)>1 and inputStr[1]=='i':
    print(3.14,end="");
    replacePi(inputStr[2:])
    return
  print(inputStr[0], end="")
  replacePi(inputStr[1:])

def main():
    inputStr = "pippxxppiixipi"
    replacePi(inputStr)

if __name__ == "__main__":
    main()

