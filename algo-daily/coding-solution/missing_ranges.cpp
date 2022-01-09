class Solution {
public:
    string formatOutput(int prev, int curr){
        if(prev==curr){
            return to_string(prev);
        }
        return to_string(prev) + "->" + to_string(curr);
    }
    vector<string> findMissingRanges(vector<int>& nums, int lower, int upper) {
        
        vector<string> result;
        int prev = lower-1;
        int n = nums.size();
        int curr;
        for(int i=0; i<=n; i++){
            int curr = i<n?nums[i]:upper+1;
            if(prev+1 <= curr-1){
                result.push_back(formatOutput(prev+1, curr-1));
            }
            
            prev = curr;
        }
        
        
        return result;
        
    }
};