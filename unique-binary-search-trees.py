#!/usr/bin/env python

__author__ = 'hbprotoss'

"""
https://oj.leetcode.com/problems/unique-binary-search-trees/

Unique Binary Search Trees

Given n, how many structurally unique BST's (binary search trees) that store values 1...n?

For example,
Given n = 3, there are a total of 5 unique BST's.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""

# Time Limit Exceeded
# import itertools
# class Solution:
#     # @return an integer
#     def numTrees(self, n):
#         sum = 0
#         for seq in itertools.permutations(range(n)):
#             if self.check(seq):
#                 sum += 1
#         return sum
#
#     def check(self, seq):
#         if len(seq) <= 1:
#             return True
#
#         p = seq[0]
#         i = 1
#         while i < len(seq) and seq[i] < p:
#             i += 1
#         border = i
#         while i < len(seq) and seq[i] > p:
#             i += 1
#
#         if i < len(seq):
#             return False
#         else:
#             return self.check(seq[1:border]) and self.check(seq[border:])

class Solution:
    # @return an integer
    def numTrees(self, n):
        dp = [1, 1]
        for i in range(2, n+1):
            total = 0
            for j in range(i):
                total += dp[j] * dp[i-j-1]
            dp.append(total)
        return dp[n]

if __name__ == '__main__':
    s = Solution()
    assert s.numTrees(2) == 2
    assert s.numTrees(3) == 5
