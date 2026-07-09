class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []

        mapper = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }

        q = deque([""])

        for digit in digits:

            size = len(q)

            for _ in range(size):

                cur = q.popleft()

                for ch in mapper[digit]:
                    q.append(cur + ch)

        return list(q)