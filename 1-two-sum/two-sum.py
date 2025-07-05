class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Brute force
        output = []
        for i in range(0,len(nums)):
            for j in range(i+1, len(nums)):
                if (nums[i] + nums[j]) == target:
                    output.append(i)
                    output.append(j)
                    break
            if len(output) > 0:
                break
        return output
