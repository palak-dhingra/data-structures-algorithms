class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        
        vector<vector<int>> result;
        sort(nums.begin(), nums.end());
        
        int n = nums.size();
        for(int i=0; i<n-2; i++){
            if(i==0 || nums[i-1]!=nums[i]){
                int a = nums[i];
                // 2 pointer approach 
                int low = i+1;
                int high = n-1;
                while(low < high){
                    int b = nums[low];
                    int c = nums[high];
                    if(a+b+c==0){
                        result.push_back({a, b, c});
                        while(low<high and nums[low]==nums[low+1]) low++;
                        while(low<high and nums[high]==nums[high-1]) high--;
                        
                        low++; 
                        high--;
                    }
                    else if(b+c<-a){
                        low++;
                    }
                    else{
                        high--;
                    }
                }
            }
            
            
        }
        return result;
        
    }
};