class Solution {
public:
    bool isLetter(char c){
        return (c>='a' and c<='z') or (c>='A' and c<='Z');
    }
    string reverseOnlyLetters(string s) {
        
        int n = s.length() -1;
        int i = 0;
        
        while(i<n){
            if(!isLetter(s[i])){
                i++;
                continue;
            }
            if(!isLetter(s[n])){
                n--;
                continue;
            }
            swap(s[i], s[n]);
            i++;
            n--;
        }
        
        return s;
        
    }
};