class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        val = min(coins)
        cnt = 1
        temp = [val]

        while True:
            if cnt == k:
                return temp[k - 1]
            
            val += 1
            for coin in coins:
                if val % coin == 0:
                    temp.append(val)
                    cnt += 1
                    break
        return -1