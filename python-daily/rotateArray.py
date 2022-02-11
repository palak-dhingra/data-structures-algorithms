def reverse(arr, s, e):
    while s<e:
        arr[s], arr[e] = arr[e], arr[s]
        s+=1
        e-=1
def rotate( arr, n):
    reverse(arr, 0, n-1)
    reverse(arr, 1, n-1)