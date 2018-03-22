# -*- coding: utf-8 -*-
'对循环表每个元素，遍历其后续元素，找出大于该元素的第一个元素'

# 立即想到的办法，没有用到栈的思想,性能不够快, O(n**2)
def get_next_greater_elements1(nums):
    length = len(nums)
    results = [-1]*length
    for i in xrange(length):
        tmp_nums = nums[i:] + nums[0:i]
        for item in tmp_nums:
            if item > nums[i] :
                results[i] = item
                break
    return results

# 使用stack，O(n)
def get_next_greater_elements(nums):
    stack, res = [], [-1]*len(nums)
    for index, num in enumerate(nums*2):
        while stack and nums[stack[-1]] < num:
            res[stack.pop()] = num
        if index < len(nums):
            stack.append(index)
    return res


nums = [1, 2, 1, 9, 10, 7]
print get_next_greater_elements(nums)