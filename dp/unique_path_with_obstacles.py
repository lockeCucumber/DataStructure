# -*- coding: utf-8 -*-
'''
长方形矩阵，左上到右下的方式数量, 每个格子为1表示是障碍，无法通过
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
'''

def get_unique_path_count_with_obstacles(obstacle_grid):
    """
    :type obstacle_grid: List[List[int]]
    :rtype: int
    """
    m = len(obstacle_grid)
    n = len(obstacle_grid[0])
    res = [[1]*n]*m

    for i in xrange(m):
        if obstacle_grid[i][0] == 1:
            for j in xrange(i, m):
                res[j][0] = 0
        break

    for i in xrange(n):
        if obstacle_grid[0][i] == 1:
            for j in xrange(i, n):
                res[0][j] = 0
        break

    for i in xrange(1, m):
        for j in xrange(1, n):
            if obstacle_grid[i][j] == 1:
                res[i][j] = 0
            else:
                res[i][j] = res[i-1][j] + res[i][j-1]
    return res[-1][-1]
            


obstacle_grid = [
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
print get_unique_path_count_with_obstacles(obstacle_grid)
