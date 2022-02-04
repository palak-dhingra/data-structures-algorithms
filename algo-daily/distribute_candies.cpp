class Solution {
public:
    int distributeCandies(vector<int>& candyType) {
        
        unordered_set<int> candy;
        for(auto x : candyType){
            candy.insert(x);
        }
        return min(candy.size(), candyType.size()/2);
        
    }
};