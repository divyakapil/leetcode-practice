class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0 # initializing left pointer
        max_length = 0 # current length of window
        map = set()

        # Time Complexity: O(n), Space Complexity: O(n)
        for right in range(len(s)): # check for duplicate, if yes then remove the previous character from the set
            while s[right] in map:
                map.remove(s[left])
                left+=1 # increment left pointer after removing duplicate character from set

            current_window_length = (right - left) + 1
            max_length = max(max_length, current_window_length)
            map.add(s[right])
        return max_length
