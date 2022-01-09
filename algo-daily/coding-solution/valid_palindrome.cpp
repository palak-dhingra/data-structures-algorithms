class Solution {
public:
    
    bool isPalindrome(string s) {
        
        int i = 0;
        int e = s.length()-1;
        
        while(i<e){
            s[i] = tolower(s[i]);
            s[e] = tolower(s[e]);
            if(!isalnum(s[i])){
                i++;
                continue;
            }
            if(!isalnum(s[e])){
                e--;
                continue;
            }
            if(s[i]!=s[e]){
                return false;
            }
            i++;
            e--;
        }
        
        return true;
        
    }
};