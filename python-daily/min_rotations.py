def min_rotations(nums):
  lo = 0
  hi = len(nums)-1
  while lo<hi:
    mid = (lo+hi)//2

    if nums[mid] < nums[hi]:
      hi = mid 
    elif nums[mid] > nums[hi]:
      lo = mid +1
    else:
      return mid
    

  return hi



def main():
  nums=[1, 2, 3, 4, 5, 6]
  print(min_rotations(nums))

if __name__ == "__main__":
    main()