class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:   
        ans = []

        for i, (prev, mtn) in enumerate(pairwise(height)):
            if prev > threshold:
                ans.append(i+1)
        
        return ans