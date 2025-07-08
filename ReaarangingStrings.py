from collections import Counter
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        # Count the frequency of each character
        count = Counter(s)
        # For example: "aaabbc" = {'a': 3, 'b': 2, 'c': 1}
        # Build a max heap based on character frequency
        # We use -freq because Python's heapq is a min-heap
        max_heap = [(-freq, char) for char, freq in count.items()]
        heapq.heapify(max_heap)
        # Now we can always pop the most frequent character first

        # Step 3: Initialize result and prev
        result = []
        prev = (0, "")

        # Step 4: Process characters in the heap
        while max_heap or prev[0] < 0:
            # If there's no character to choose from and previous is still pending
            # Then it's impossible to rearrange without repeating characters
            if not max_heap and prev[0] < 0:
                return ""
            # Pop the most frequent character
            freq, char = heapq.heappop(max_heap)
            result.append(char)  # Add it to the result string

            # If the previous character still has remaining frequency,
            # push it back into the heap for future use
            if prev[0] < 0:
                heapq.heappush(max_heap, prev)

            # Update the prev character with current one, reducing its count by 1
            # Because we used it once now
            prev = (freq + 1, char)  # freq is negative, so adding 1 moves toward 0

        # Join the string to get final output
        return "".join(result)
