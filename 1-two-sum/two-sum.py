class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsDict = {}
        for index,value in enumerate(nums):
            if value not in numsDict:
                numsDict[value] = [index]
            else:
                numsDict[value].append(index)
                
        for index,value in enumerate(nums):
            print(target - value)
            if (target - value) in numsDict:
                for i in numsDict[target - value]:
                    if i != index:
#                        output = [index,i]
#                        output.sort()
                        return [index,i]