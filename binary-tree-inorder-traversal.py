#!/usr/bin/env python

__author__ = 'hbprotoss'


"""
Binary Tree Inorder Traversal
https://oj.leetcode.com/problems/binary-tree-inorder-traversal/

Given a binary tree, return the inorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [1,3,2].

Note: Recursive solution is trivial, could you do it iteratively?
"""

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def inorderTraversal(self, root):
        if not root:
            return []
        ret = []
        stack = []

        node = root
        while True:
            while node:
                stack.append(node)
                node = node.left

            while True:
                top = stack.pop()
                ret.append(top.val)
                if top.right:
                    node = top.right
                    break
                if len(stack) == 0:
                    return ret
