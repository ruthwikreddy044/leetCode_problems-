
class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        ans = []
        for x in nums1:
            for j in range(len(nums2)):
                if nums2[j] == x:
                    for k in range(j + 1, len(nums2)):
                        if nums2[k] > x:
                            ans.append(nums2[k])
                            break
                    else:
                        ans.append(-1)
                    break
        return ans
                             


        

        