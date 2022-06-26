class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashMap = {}
        for i, n in enumerate(nums):
            if n in hashMap and abs(hashMap[n] - i) <= k :
                return True
            else:
                hashMap[n] = i
        
        return False