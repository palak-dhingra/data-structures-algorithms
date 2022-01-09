class Solution {
public:
    bool isPowerOfThree(int n) {
        // n = 3^i
        // i = log10(n)/log10(3)
        double v =  (log10(n)/log10(3));
        return fmod(v,1)==0;
    }
};