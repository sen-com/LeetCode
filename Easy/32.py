#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i, num in enumerate(nums):
            if num < target:
                continue
            elif num >= target:
                return i
        return i+1

