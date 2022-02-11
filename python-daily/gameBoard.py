def gameBoard(start, end):
  if start==end:
    return 1
  if start > end:
    return 0
  
  count = 0
  for i in range(1, 7):
    count += gameBoard(start+i, end)

  return count
  

def main():
  print(gameBoard(0, 3))

if __name__ == "__main__":
    main()

