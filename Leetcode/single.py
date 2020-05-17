# Find single number.

class Solution:
    def singleNumber(self, nums):
        # XOR of all numbers will return number that does not repeat.
        # eg: a xor b xor a = b [because a xor a = 0 and b xor 0 = b]
        answer = 0
        for item in nums:
            answer = answer ^ item
        return answer

x = Solution()
print(x.singleNumber([1,2,1,2,4]))
        
        