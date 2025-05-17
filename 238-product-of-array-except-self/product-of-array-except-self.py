# class Solution:   Space complexity: O(N), Time complexity: O(N)
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         prefixMultArrFw = []
#         prefixMultArrBw = [0] * len(nums)
#         for index in range(len(nums)):
#             if index == 0:
#                 prefixMultArrFw.append(nums[index])
#                 prefixMultArrBw[len(nums)-1] = nums[len(nums)-1]
#             else:
#                 prefixMultArrFw.append(prefixMultArrFw[index-1]*nums[index])

#         for index in range(len(nums)-1, -1, -1):
#             if index == (len(nums)-1):                
#                 prefixMultArrBw[index] = nums[index]
#             else:
#                 prefixMultArrBw[index] = prefixMultArrBw[index+1]*nums[index]

#         for index in range(len(nums)):

#                 if index == 0:
#                     nums[index] = prefixMultArrBw[index+1]
#                 elif index + 1 < len(nums):
#                     nums[index] = prefixMultArrFw[index-1] * prefixMultArrBw[index+1]
#                 else:
#                     nums[index] = prefixMultArrFw[index-1]

#         return nums


class Solution: # Time complexity: O(N), Space complexity: O(1)
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixMultArrFw = [1]
        counter = 1
        rightSuffix = 1

        # Creating the left prefix Mulitply matrix
        for index in range(len(nums)):
            if counter < len(nums):
                prefixMultArrFw.append(prefixMultArrFw[index] * nums[index])
                counter += 1
            else:
                break
     
        for index in range(len(nums)-1, -1, -1):   
            prefixMultArrFw[index] = prefixMultArrFw[index] * rightSuffix
            if index-1 >= 0:
                rightSuffix *= nums[index]
        return prefixMultArrFw















