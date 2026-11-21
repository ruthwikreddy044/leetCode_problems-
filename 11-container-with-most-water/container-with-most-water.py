class Solution:
    def maxArea(self, height: list[int]) -> int:
    
        maxi=0
        i=0
        r=len(height)-1
        
        while i<r:
            w=r-i
            h=min(height[i],height[r])
            aera=h*w
            maxi=max(maxi,aera)
            if height[i]<height[r]:
                i=i+1
            else:
                r=r-1    
        return maxi    










