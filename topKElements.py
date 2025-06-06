class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums) # get frequency count
        return [val[0] for val in count.most_common(k)] # get the values of those counts
