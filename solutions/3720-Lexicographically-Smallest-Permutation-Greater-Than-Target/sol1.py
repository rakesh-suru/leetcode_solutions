class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        cnt = Counter(s)
        n = len(target)

        for i in range(n):
            if cnt[target[i]]:
                cnt[target[i]] -= 1
                continue

            bigger = [c for c in cnt if c > target[i] and cnt[c]]

            if bigger:
                c = min(bigger)
                cnt[c] -= 1

                return (
                    target[:i]
                    + c
                    + ''.join(ch * cnt[ch] for ch in sorted(cnt))
                )

            break

        cnt = Counter(s)

        for i in range(n - 1, -1, -1):
            for j in range(i):
                cnt[target[j]] -= 1

            bigger = [c for c in cnt if c > target[i] and cnt[c]]

            if bigger:
                c = min(bigger)
                cnt[c] -= 1

                return (
                    target[:i]
                    + c
                    + ''.join(ch * cnt[ch] for ch in sorted(cnt))
                )

            cnt = Counter(s)

        return ""