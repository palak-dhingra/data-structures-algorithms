def printAllSubarrays(arr):
  n = len(arr)
  i = 0
  while i<n:
    j = i
    while j<n:
      for k in range(i, j+1):
        print(arr[k], end=" ")
      
      j+=1
      print()
    i+=1
    print()    
  

if __name__=="__main__":
  arr = [1, 3, 5, 7, 9]
  printAllSubarrays(arr)