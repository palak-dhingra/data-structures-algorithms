class Solution {
public:
    bool isAnagram(string s, string t) {
        
        if(s.length()!=t.length()){
            return false;
        }
        
        vector<int>st_map(26, 0);
        for(int i=0; i<s.length(); i++){
            st_map[s[i]-'a']++;
            st_map[t[i]-'a']--;
        }
        
        for(int i=0; i<26; i++){
            if(st_map[i]<0){
                return false;
            }
        }
        return true;
        
    }
};