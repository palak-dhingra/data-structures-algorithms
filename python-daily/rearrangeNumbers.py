def rearrange(arr, n):
    negative_ptr = 0

    for i in range(n):
        if arr[i] < 0:
            arr[negative_ptr], arr[i] = arr[i], arr[negative_ptr]
            negative_ptr += 1
            i -= 1
        

def main():
    # Your code goes here
    arr = [-1, 2, -3, 4, 5, 6, -7, 8, 9]
    n = len(arr)
    rearrange(arr, n)
    print(arr)
    
if __name__ == "__main__":
    main()

