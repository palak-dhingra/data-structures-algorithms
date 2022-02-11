def getMinMax(nums):
  n = len(nums)
  if n==0:
    return None, None
  num_min = num_max = nums[0]

  for ele in nums:
    if ele < num_min:
      num_min = ele
    if ele > num_max:
      num_max = ele

  return num_min, num_max

def main():
  nums = [1000, 11, 445, 1, 330, 3000]
  num_min, num_max = getMinMax(nums)
  print("minimum number - ", num_min)
  print("maximum number - ", num_max)
  

if __name__ == "__main__":
    main()