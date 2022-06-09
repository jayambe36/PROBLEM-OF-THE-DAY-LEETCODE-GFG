class Solution:
    def arraySign(self, nums):
        answer = 1
        for i in range(len(nums)):
            answer = answer*nums[i]
        if answer > 0:
            return 1
        if answer < 0:
            return -1
        if answer == 0:
            return 0
