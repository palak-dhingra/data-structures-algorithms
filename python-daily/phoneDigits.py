def phoneDigits(inputStr, outputStr):
  phoneBook = ["", "", "ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
  
  if len(inputStr)==0:
    print(outputStr)
    return
  
  number = inputStr[0]
  possibleStr = phoneBook[int(number)]

  for i in possibleStr:
    phoneDigits(inputStr[1:], outputStr+i)





def main():
  inputStr = "27"
  phoneDigits(inputStr, "")

if __name__ == "__main__":
    main()

