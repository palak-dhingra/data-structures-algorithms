class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int n = s.size() -1;
        int l = 0;
        int r = 0;
        int max_len = 0;
        unordered_map<char, int> s_map;
        while(r<=n){
            char c = s[r];
            if(s_map.find(c) != s_map.end()){
                l = max(s_map[c]+1, l);
            }
            s_map[c] = r;
            max_len = max(max_len, r-l+1);
            r++;
        }
        return max_len;
    }
};