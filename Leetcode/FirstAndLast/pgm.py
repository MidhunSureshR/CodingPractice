from typing import List

class Solution:
    
    def middle(self, lb, ub):
        return (lb + ub) // 2

    def binary_search(self, array, key):
        lb, ub = 0, len(array)-1
        while lb <= ub:
            mid = self.middle(lb, ub)
            if array[mid] == key:
                return mid
            elif array[mid] < key:
                lb = mid + 1
            else:
                ub = mid - 1
        return -1
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        initial = self.binary_search(nums, target)
        if initial == -1:
            return [-1, -1]

        # Find start and end
        min = max = initial
        while True:
            x = self.binary_search(nums[0:min], target)
            if x == -1:  
                break      
            min = x
        while True:
            x = self.binary_search(nums[max+1:], target)
            if x == -1:
                break
            min = x
        return [min, max]        
    


def test():
    input1 = [5,7,7,8,8,10]
    target1 = 8
    _ = Solution()
    try:
        ans = _.searchRange(input1,target1)
        if ans != [3, 4]:
            print("Test Failed due to Wrong Answer.","Your answer = ",ans)
        else:
            print("Test Passed. Deploy.")
    except Exception:
        print("Test Failed due to Error.")
        raise
test()