class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freq = [0] * 26

        for(a, b) in zip(s, t):
            freq[ord(a) - ord('a')] += 1
            freq[ord(b) - ord('a')] -=1
        
        for val in freq:
            if val != 0:
                return False
        return True
        