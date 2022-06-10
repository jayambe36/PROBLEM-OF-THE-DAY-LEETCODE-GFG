class Solution:
    def isSameAfterReversals(self, num):
        tmp = str(num)
        tmp = int(tmp[::-1])
        tmp = str(tmp)
        tmp = tmp[::-1]
        if int(tmp) == num:
            return True
        else:
            return False