def moveAllX(inputStr):
  if(len(inputStr)==0):
    return ""

  c = inputStr[0]
  outputStr = moveAllX(inputStr[1:])
  if c =='x':
    return outputStr + c
  return c + outputStr
  
  

def main():
    inputStr = "axxbdxcefxhix"
    print(moveAllX(inputStr))

if __name__ == "__main__":
    main()

