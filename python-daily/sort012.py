class Solution:
    def sort012(self,arr,n):
        low = 0
        i = 0
        high = n-1
        
        while(i<=high):
            if(arr[i]==1):
                i+=1
            elif arr[i]==0:
                arr[low], arr[i] = arr[i], arr[low]
                i+=1
                low+=1
            elif arr[i]==2:
                arr[high], arr[i] = arr[i], arr[high]
                high-=1
                