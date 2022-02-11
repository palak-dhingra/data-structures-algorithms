def generateAllSubstrings (inputStr, outputStr):
  if len(inputStr) == 0:
    print(outputStr, end=", ")
    return

  c = inputStr[0]
  ros = inputStr[1:]
  generateAllSubstrings(ros, outputStr+c)
  generateAllSubstrings(ros, outputStr)
  
  

def main():
    inputStr = "ABC"
    outputStr = ""
    generateAllSubstrings(inputStr, outputStr)

if __name__ == "__main__":
    main()

