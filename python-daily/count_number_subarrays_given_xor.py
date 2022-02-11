test_cases =[ 
  {
    "input" : 
    {
      "arr":[4, 2, 2, 6, 4],
      "k" : 6
    },
    "output" : 4 
  },
  {
    "input" : 
    {
      "arr": [5, 6, 7, 8, 9],
      "k":5
    },
    "output" : 2
}]

def count_subarray_with_xor(arr, k):
  xxor = 0
  cnt = 0
  arr_dict = dict()
  # y ^ k = xxor
  # y = xxor ^ k

  for ele in arr:
    xxor = xxor ^ ele
    if xxor == k:
      cnt += 1
    
    if xxor ^ k in arr_dict:
      cnt += arr_dict[xxor^k]
    
    arr_dict[xxor] = arr_dict.get(xxor, 0) + 1

  return cnt

print(count_subarray_with_xor([4, 2, 2, 6, 4], 6))

print(count_subarray_with_xor([5, 6, 7, 8, 9], 5))