def generateAllSubStringASCII(inputStr, outputStr):
  if(len(inputStr)==0):
    print(outputStr, end=",")
    return

  c = inputStr[0]
  ros = inputStr[1:]
  generateAllSubStringASCII(ros, outputStr)
  generateAllSubStringASCII(ros, outputStr+c)
  generateAllSubStringASCII(ros, outputStr+str(ord(c)))
  
  

def main():
    inputStr = "AB"
    outputStr = ""
    generateAllSubStringASCII(inputStr, outputStr)

if __name__ == "__main__":
    main()

