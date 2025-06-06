class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {} # creating an empty hashmap
        for i,n in enumerate(nums): 
            difference = target - n
            if difference in hashMap: #checking if the difference is present in the hashMap or not
                return [hashMap[difference],i] #if diff is found then we return the value and the index
            hashMap[n] = i #else we add the value and the index associated in the hash map
