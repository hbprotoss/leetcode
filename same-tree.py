#!/usr/bin/env python

__author__ = 'hbprotoss'

"""
https://oj.leetcode.com/problems/same-tree/

Same Tree

Given two binary trees, write a function to check if they are equal or not.

Two binary trees are considered equal if they are structurally identical and the
nodes have the same value.
"""

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param p, a tree node
    # @param q, a tree node
    # @return a boolean
    def isSameTree(self, p, q):
        if p is None or q is None:
            return p == q

        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left)\
               and self.isSameTree(p.right, q.right)
