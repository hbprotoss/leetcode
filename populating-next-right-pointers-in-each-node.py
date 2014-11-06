#!/usr/bin/env python

__author__ = 'hbprotoss'

"""
Populating Next Right Pointers in Each Node
https://oj.leetcode.com/problems/populating-next-right-pointers-in-each-node/

Given a binary tree

    struct TreeLinkNode {
      TreeLinkNode *left;
      TreeLinkNode *right;
      TreeLinkNode *next;
    }
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Note:

You may only use constant extra space.
You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).
For example,
Given the following perfect binary tree,
         1
       /  \
      2    3
     / \  / \
    4  5  6  7
After calling your function, the tree should look like:
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \  / \
    4->5->6->7 -> NULL
"""

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        if not root:
            return

        queues = [[],]*2
        cur_idx = 0
        node = root
        queues[cur_idx].append(node)

        while True:
            cur_queue = queues[cur_idx]
            next_queue = queues[(cur_idx + 1) % 2]
            stop = False
            for idx, n in enumerate(cur_queue):
                if n.left:
                    next_queue.append(n.left)
                else:
                    stop = True

                if n.right:
                    next_queue.append(n.right)
                n.next = cur_queue[idx+1] if idx < len(cur_queue) - 1 else None
            if stop:
                break

            queues[cur_idx] = []
            cur_idx = (cur_idx + 1) % 2

if __name__ == '__main__':
    total = 7
    nodes = [TreeNode(n) for n in range(total + 2)]
    for i in range(1, total / 2 + 1):
        
