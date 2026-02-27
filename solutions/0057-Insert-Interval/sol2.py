class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        intervals.append(newInterval)
        intervals.sort(key=lambda x: x[0])
        
        merged = [intervals[0]]
        
        for s, e in intervals[1:]:
            last = merged[-1]
            
            if s <= last[1]:
                last[1] = max(last[1], e)
            else:
                merged.append([s, e])
        
        return merged