#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Solution:
    def removeDuplicates(self, nums):
        x = 1
        for i in range(len(nums)-1):
            if(nums[i]!=nums[i+1]):
                nums[x] = nums[i+1]
                x+=1
        return(x)


# In[2]:


nums = [1,1,1,2,3,4,5,5,6,6]


# In[3]:


test = Solution()


# In[4]:


set_len = test.removeDuplicates(nums)


# In[5]:


nums[:set_len]

