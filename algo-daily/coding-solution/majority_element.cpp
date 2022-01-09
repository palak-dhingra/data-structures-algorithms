class Solution {
public:
    int majorityElement(vector<int>& nums) {
        
        int m_ele = 0;
        int count = 0;
        for(auto x : nums){
            
            if(count == 0){
                m_ele = x;
            }
            
            count += (x==m_ele) ? 1 : -1;
        }
        return m_ele;
        
    }
};