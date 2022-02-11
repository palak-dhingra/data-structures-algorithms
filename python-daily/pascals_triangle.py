class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        temp = [1]
        result.append(temp)
        for i in range(1, numRows):
            temp = []
            temp.append(1)
            temp2 = result[i-1]
            for j in range(1, i):
                temp.append(temp2[j-1] + temp2[j])
            temp.append(1)
            result.append(temp)
        
        return result