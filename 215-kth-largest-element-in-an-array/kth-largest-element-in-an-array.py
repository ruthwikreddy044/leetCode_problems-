class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        l=[]
        for i in nums:
            l.append(-i)
        heapq.heapify(l)
        c=1
        while c<k:
            heapq.heappop(l)
            c=c+1
        return   -heapq.heappop(l)   


            
        