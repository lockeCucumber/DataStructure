# -*- coding: utf-8 -*-
'''
Given n non-negative integers a1, a2, ..., an, 
where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
Find two lines, which together with x-axis forms a container, 
such that the container contains the most water.
Note: You may not slant the container and n is at least 2.
'''

def get_max_area(height_list):
    max_area = 0
    l, r = 0, len(height_list-1)
    while l < r:
        area = (r-l) * min(height_list[l], height_list[r])
        if area > max_area:
            max_area = area
        if height_list[l] < height_list[r]:
            l += 1
        else:
            r -= 1
    return max_area