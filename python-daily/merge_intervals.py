class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result_intervals = []
        start = intervals[0][0]
        end = intervals[0][1]
        for ele in intervals:
            if end>=ele[0]:
                end = max(end, ele[1])
            else:
                result_intervals.append([start, end])
                start = ele[0]
                end = ele[1]
        result_intervals.append([start, end])
        return result_intervals