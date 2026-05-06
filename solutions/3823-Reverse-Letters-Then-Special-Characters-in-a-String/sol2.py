class Solution:
    def reverseByType(self, s: str) -> str:
        arr = list(s)
        n = len(arr)

        left, right = 0, n - 1
        while left < right:
            if arr[left].islower() and arr[right].islower():
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1
            elif not arr[left].islower():
                left += 1
            else:
                right -= 1

        left, right = 0, n - 1
        while left < right:
            if not arr[left].isalnum() and not arr[right].isalnum():
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1
            elif arr[left].isalnum():
                left += 1
            else:
                right -= 1

        return "".join(arr)