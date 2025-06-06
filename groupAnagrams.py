class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        anagram_map = defaultdict(list)
        for w in strs:
            count = [0] * 26 #count alphabets from a-z and 26 alphabets 
            for char in w: #check for the character present in word
                count[ord(char) - ord('a')] +=1 #count the characters
            key = tuple(count) #store the count in a var
            anagram_map[key].append(w) #if the count matches then group the words
        return list(anagram_map.values()) 
