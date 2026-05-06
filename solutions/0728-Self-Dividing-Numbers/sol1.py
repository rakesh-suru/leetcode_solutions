class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []

        for num in range(left, right + 1):
            temp = str(num)

            if "0" in temp:
                continue
            
            flag = True
            for ch in temp:
                if num % int(ch) != 0:
                    flag = False
            if flag:
                ans.append(num)
        
        return ans