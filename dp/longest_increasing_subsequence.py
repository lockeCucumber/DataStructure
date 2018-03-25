# -*- coding: utf-8 -*-
'给定一个数字list，获取其递增子集中长度最大的长度'

def get_length_of_lis(nums):
    '''
    :type nums: list[int]
    :rtype int
    '''
    length = len(nums)
    if length == 0:
        return 0

    dp = [1] * length
    for i in xrange(1, length):
        tmp = [1] * i
        for j in xrange(i):
            if nums[j] < nums[i]:
                tmp[j]= dp[j] + 1
        dp[i] = max(tmp)
    return max(dp)

nums = [1,2,3,2]
print get_length_of_lis(nums)
    
