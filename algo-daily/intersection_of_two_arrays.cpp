class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        vector<int> result;
        unordered_set<int> set_nums1;
        for(auto x : nums1){
            set_nums1.insert(x);
        }
        for(auto x : nums2){
            if(set_nums1.find(x)!=set_nums1.end()){
                set_nums1.erase(x);
                result.push_back(x);
            }
        }
        
        
        return result;
        
    }
};