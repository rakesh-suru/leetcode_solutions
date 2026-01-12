class Solution:
    def maximum69Number (self, num: int) -> int:
        switch_map = {'9': '6', '6': '9'}
        num_str = [s for s in str(num)]
        
        for i, n in enumerate(num_str):
            if n == '6':
                num_str[i] = '9'
                break
        return int(''.join(num_str))