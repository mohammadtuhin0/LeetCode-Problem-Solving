from typing import List
from collections import Counter

class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        total = sum(sum(row) for row in grid)

        # ---------- Horizontal ----------
        top_sum = 0
        top_cnt = Counter()
        bottom_cnt = Counter(val for row in grid for val in row)

        for i in range(m - 1):
            for val in grid[i]:
                top_sum += val
                top_cnt[val] += 1
                bottom_cnt[val] -= 1

            bottom_sum = total - top_sum

            if top_sum == bottom_sum:
                return True

            diff = abs(top_sum - bottom_sum)

            # remove from top
            if top_sum > bottom_sum:
                if top_cnt[diff] > 0:
                    # single row top
                    if i == 0:
                        row = grid[0]
                        if row[0] == diff or row[-1] == diff:
                            return True
                    # single column grid
                    elif n == 1:
                        col = [grid[k][0] for k in range(i+1)]
                        if col[0] == diff or col[-1] == diff:
                            return True
                    else:
                        return True

            # remove from bottom
            else:
                if bottom_cnt[diff] > 0:
                    # single row bottom
                    if i == m - 2:
                        row = grid[m - 1]
                        if row[0] == diff or row[-1] == diff:
                            return True
                    # single column grid
                    elif n == 1:
                        col = [grid[k][0] for k in range(i+1, m)]
                        if col[0] == diff or col[-1] == diff:
                            return True
                    else:
                        return True

        # ---------- Vertical ----------
        left_sum = 0
        left_cnt = Counter()
        right_cnt = Counter(val for row in grid for val in row)

        for j in range(n - 1):
            for i in range(m):
                val = grid[i][j]
                left_sum += val
                left_cnt[val] += 1
                right_cnt[val] -= 1

            right_sum = total - left_sum

            if left_sum == right_sum:
                return True

            diff = abs(left_sum - right_sum)

            # remove from left
            if left_sum > right_sum:
                if left_cnt[diff] > 0:
                    # single column left
                    if j == 0:
                        col = [grid[i][0] for i in range(m)]
                        if col[0] == diff or col[-1] == diff:
                            return True
                    # single row grid
                    elif m == 1:
                        row = grid[0][:j+1]
                        if row[0] == diff or row[-1] == diff:
                            return True
                    else:
                        return True

            # remove from right
            else:
                if right_cnt[diff] > 0:
                    # single column right
                    if j == n - 2:
                        col = [grid[i][n - 1] for i in range(m)]
                        if col[0] == diff or col[-1] == diff:
                            return True
                    # single row grid
                    elif m == 1:
                        row = grid[0][j+1:]
                        if row[0] == diff or row[-1] == diff:
                            return True
                    else:
                        return True

        return False