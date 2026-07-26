class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        arr = ['1'] + list(s) + ['1']
        m = len(arr)

        ans = s.count('1')

        i = 1
        while i < m - 1:

            if arr[i] == '1':
                j = i

                while j < m and arr[j] == '1':
                    j += 1

                if j < m and arr[i - 1] == '0' and arr[j] == '0':

                    temp = arr[:]

                    for k in range(i, j):
                        temp[k] = '0'

                    L = i
                    while L > 0 and temp[L - 1] == '0':
                        L -= 1

                    R = j - 1
                    while R + 1 < m and temp[R + 1] == '0':
                        R += 1

                    for k in range(L, R + 1):
                        temp[k] = '1'

                    ans = max(ans, temp.count('1') - 2)

                i = j
            else:
                i += 1

        return ans