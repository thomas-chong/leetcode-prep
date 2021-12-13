# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 1
        j = n
        while i <= j:
            q = (i + j) // 2
            if isBadVersion(q) == True and isBadVersion(q-1) == False:
                return q
            elif isBadVersion(q) == True and isBadVersion(q-1) == True:
                j = q - 1
            else:
                i = q + 1