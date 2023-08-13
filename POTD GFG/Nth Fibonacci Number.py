class Solution:
    def nthFibonacci(self, n : int) -> int:
        # code here 
        a=0
        b=1
        mod=10**9+7
        if n==1:
            return 1
        for i in range(2,n+1):
            b,a=(b+a)%mod,b
        return b 
