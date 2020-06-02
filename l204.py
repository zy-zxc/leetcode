import math


class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0 or n==1:
            return 0
        count=0
        f=[1]*(n-1)
        f[0]=0
        for i in range(2,int(math.sqrt(n))+1):
            if f[i-1]:
                for j in range(i*i,n,i):
                    f[j-1]=0
        for i in range(n-1):
            if f[i]:
                count+=1
        print(f)
        return count

print(Solution().countPrimes(10))