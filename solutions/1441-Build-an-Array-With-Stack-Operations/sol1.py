class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans = []
        steps = []
        i = 0
        curr = 1

        while i < len(target):

            if target[i] == curr:
                steps.append("Push")
                curr += 1
                i += 1

            elif target[i] > curr:
                steps.append("Push")
                steps.append("Pop")
                curr += 1
            
        return steps