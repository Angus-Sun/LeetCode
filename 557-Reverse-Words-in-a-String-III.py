class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        words_final = []
        for word in words:
            words_final.append(word[::-1])
        
        return " ".join(words_final)
