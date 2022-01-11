class Solution{
    public:
    int maxLen(vector<int>&A, int n)
    {   
        unordered_map<int, int> prefixSum;
        int idx = -1;
        int max_count = 0;
        
        int sum = 0;
        for(int i=0; i<A.size(); i++){
            sum += A[i];
            int count = 0;
            if(sum==0){
                max_count = i+1;
            }
            else{
                if(prefixSum.find(sum)!=prefixSum.end()){
                    count = i - prefixSum[sum];
                    max_count = max(max_count, count);
                 
                }
                else{
                    prefixSum.insert({sum, i});
                }   
            }
        }
        
        return max_count;
    }
};