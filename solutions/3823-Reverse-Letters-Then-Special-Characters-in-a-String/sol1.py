class Solution:
    def reverseByType(self, s: str) -> str:
        temp = list(s)
        left, right = 0, len(temp) - 1

        while left < right:
            if temp[left].isalnum() and temp[right].isalnum():
                temp[left], temp[right] = temp[right], temp[left]
                left += 1
                right -= 1

            elif not temp[left].isalnum():
                left += 1

            elif not temp[right].isalnum():
                right -= 1


        left, right = 0, len(temp) - 1

        while left < right:
            if not temp[left].isalnum() and not temp[right].isalnum():
                temp[left], temp[right] = temp[right], temp[left]
                left += 1
                right -= 1

            elif temp[left].isalnum():
                left += 1

            elif temp[right].isalnum():
                right -= 1
                
        return "".join(temp)