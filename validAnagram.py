class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # first step is to check if the length of both strings are same or not
        if len(s) != len(t):
            return False

        # create dictionary
        frequency_count_s = {} # count characters in s
        frequency_count_t = {} # count characters in t
        
        # Check if 'a' exists in count_s
        # If yes, get its value 
        # else set the count as 0 for that value and increment it with 1
        for c in s:
            frequency_count_s[c] = frequency_count_s.get(c,0) + 1
        for c in t:
            frequency_count_t[c] = frequency_count_t.get(c,0) + 1
        
        return frequency_count_s == frequency_count_t
