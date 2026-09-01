class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        cnt = Counter(s)
        n = len(s)

        for i in range(n):
            ch = target[i]

            if cnt[ch] > 0:
                cnt[ch] -= 1
                continue

            bigger = [c for c in cnt if c > ch and cnt[c] > 0]

            if bigger:
                c = min(bigger)
                cnt[c] -= 1

                return target[:i] + c + ''.join(
                    c * cnt[c] for c in sorted(cnt)
                )
            break

        cnt = Counter(s)

        for i in range(n - 1, -1, -1):
            temp = cnt.copy()
            possible = True

            for j in range(i):
                if temp[target[j]] == 0:
                    possible = False
                    break
                temp[target[j]] -= 1

            if not possible:
                continue

            bigger = [
                c for c in temp
                if c > target[i] and temp[c] > 0
            ]

            if bigger:
                c = min(bigger)
                temp[c] -= 1

                return target[:i] + c + ''.join(
                    c * temp[c] for c in sorted(temp)
                )

        return ""