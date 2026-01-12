class Solution:
	def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
		high_enough = max(candies) - extraCandies
		return [i >= high_enough for i in candies]