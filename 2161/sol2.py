class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
	s = []
	p = []
	l = []
	for i in nums:
		if i < nums:
			s.append(i)
		elif i > nums:
			l.append(i)
		else:
			p.append(i)
	return s+p+l