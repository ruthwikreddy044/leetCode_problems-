class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        l=[]
        for i in gifts:
            l.append(-i)
        heapq.heapify(l)
        for i in range(k):
            a=-heapq.heappop(l)
            b=floor(a**0.5)
            heapq.heappush(l,-b)
        return -sum(l)        
        
        