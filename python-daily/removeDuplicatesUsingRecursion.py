def removeAllDuplicates(inputStr):
  if(len(inputStr)==1):
    return inputStr;

  c = inputStr[0]
  outputStr = removeAllDuplicates(inputStr[1:])
  if(c == outputStr[0]):
    return outputStr;
  return c+outputStr
  
  

def main():
    inputStr = "aaaabbbeeecddd"
    print(removeAllDuplicates(inputStr))

if __name__ == "__main__":
    main()

