class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        flip_count = 0
        mask = 1
        
        for _ in range(32):  # Assuming 32-bit integers
            start_bit = bool(start & mask)
            goal_bit = bool(goal & mask)
            
            if start_bit != goal_bit:
                flip_count += 1
            
            mask <<= 1
        
        return flip_count