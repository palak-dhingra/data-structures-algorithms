def triplets(arr, targetSum):
  n = len(arr)
  arr.sort();
  result = list()

  for i in range(n-2):
    j = i+1
    k = n-1

    # search for pair with sum targetSum
    while(j<k):
      csum = arr[i] + arr[j] + arr[k]
      if csum ==targetSum:
        result.append([arr[i], arr[j], arr[k]])
        j += 1
        k -= 1
      elif csum > targetSum:
        k -=1
      else:
        j +=1 

  return result





def main():
  arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 15] 
  target = 18
  result = triplets(arr, target)
  print(result)
   

if __name__ == "__main__":
    main()

