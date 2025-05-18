class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_dict = {}
        for val in nums:
            if val not in nums_dict:
                nums_dict[val] = 1
            else:
                return True
        return False
