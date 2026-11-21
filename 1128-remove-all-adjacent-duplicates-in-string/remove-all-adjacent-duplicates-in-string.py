class Solution:
    def removeDuplicates(self, s: str) -> str:
        a=[]
        for i in s:
            if a  and a[-1]==i:
                a.pop()
            else:
                a.append(i)    
        b=""
        for i in a:
            b=b+i
        return b    
        
    
        

        
        

        

        
       
       
      
        


        