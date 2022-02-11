def merge(arr, start, end):
  total_count = 0
  mid = (start+end)//2
  temp = []
  i = start
  j = mid+1
  while i<=mid and j<=end:
    if arr[i]>arr[j]:
      total_count += (mid-i+1)
      temp.append(arr[j])
      j+=1
    else:
      temp.append(arr[i])
      i +=1

  while i<=mid:
    temp.append(arr[i])
    i+=1
  while j<=end:
    temp.append(arr[j])
    j+=1
  i = 0
  while start<=end:
    arr[start]=temp[i]
    start+=1
    i+=1
  return total_count
def count_inversions(arr, start, end):
  if start<end:
    mid = (start+end)//2
    left_count = count_inversions(arr, start, mid)
    right_count = count_inversions(arr, mid+1, end)
    total = left_count + right_count + merge(arr, start, end)
    return total
  
  return 0;


arr = [8, 4, 2, 1]
n = len(arr)-1
# expected output = 6

count = count_inversions(arr, 0, n)
print(count)