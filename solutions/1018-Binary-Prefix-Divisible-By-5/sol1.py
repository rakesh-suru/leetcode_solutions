class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        temp = []
        for i in range(len(nums)):
            temp.append(int("".join(map(str, nums[:i+1])), 2))
        ans = []
        for num in temp:
            if num % 5 == 0:
                ans.append(True)
            else:
                ans.append(False)
        return ans
