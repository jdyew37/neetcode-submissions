class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashmap = {}

        for n in range(len(nums)):
            if nums[n] in hashmap:
                hashmap[nums[n]] += 1
            else:
             hashmap[nums[n]] = 1
            if n == len(nums)-1:
             for key, value in hashmap.items():
                 if value == 1:
                      return key
        return 0

                
            


        