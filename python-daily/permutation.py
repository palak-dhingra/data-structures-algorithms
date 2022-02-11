def permute(inputStr, outputStr):
  if len(inputStr)==0:
    print(outputStr)
    return 

  for i in range(len(inputStr)):
    c = inputStr[i]
    inter = list(inputStr)
    inter = inputStr[:i] + inputStr[i+1:]
    permute(str(inter), outputStr+c)


def main():
  inputStr = "ABC"
  outputStr = ""
  permute(inputStr, outputStr)
   

if __name__ == "__main__":
    main()

