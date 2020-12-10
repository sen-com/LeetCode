#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        x = 0
        for i in range(len(nums)):
            if not nums[i]==val:
                nums[x] = nums[i]
                x+=1
        return x

