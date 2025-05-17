class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_sum_arr = [nums[0]]
        for index,value in enumerate(nums):
            if index != 0:
                self.prefix_sum_arr.append(value+self.prefix_sum_arr[index-1])
        

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.prefix_sum_arr[right]
        else:
            return (self.prefix_sum_arr[right] - self.prefix_sum_arr[left-1])
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)