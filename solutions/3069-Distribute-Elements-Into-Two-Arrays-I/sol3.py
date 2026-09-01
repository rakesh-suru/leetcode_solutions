class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1 = deque([nums[0]])
        arr2 = deque([nums[1]])

        for num in nums[2:]:
            if arr1[-1] > arr2[-1]:
                arr1.append(num)
            else:
                arr2.append(num)

        return list(arr1) + list(arr2)