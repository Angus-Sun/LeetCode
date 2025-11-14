class Solution:
    def romanToInt(self, s: str) -> int:
        numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        sum = 0
        for i in range(len(s)-1):
            if (numerals[s[i]] < numerals[s[i+1]]):
                sum -= numerals[s[i]]
            else:
                sum += numerals[s[i]]
        sum += numerals[s[len(s)-1]]
        return sum
                
