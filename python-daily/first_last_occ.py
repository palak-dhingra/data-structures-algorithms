def last_occ(nums, key):
  lo = 0
  hi = len(nums)-1
  res = -1
  while lo<=hi:
    mid = (lo+hi)//2
    
    if nums[mid] == key:
      lo = mid+1
      res = mid
    elif nums[mid]<key:
      lo = mid+1
    else:
      hi = mid-1

  return res

def first_occ(nums, key):
  lo = 0
  hi = len(nums)-1
  res = -1
  while lo<=hi:
    mid = (lo+hi)//2
    
    if nums[mid] == key:
      hi = mid-1
      res = mid
    elif nums[mid]<key:
      lo = mid+1
    else:
      hi = mid-1

  return res

def first_last_occ(nums, key):
  return [first_occ(nums, key), last_occ(nums, key)]



def main():
  nums=[3, 4, 6, 6, 6, 6, 7, 8, 9]
  key=6
  print(first_last_occ(nums, key))

if __name__ == "__main__":
    main()