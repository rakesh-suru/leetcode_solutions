class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        
        result = []

        answer = 0
        for i in range(0,n):
            num = (start + 2 * i)
            answer ^= num
        print(result)
  
        return (answer)