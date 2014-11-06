#!/usr/bin/env python

__author__ = 'hbprotoss'


"""
Linked List Cycle
https://oj.leetcode.com/problems/linked-list-cycle/

Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        if not head:
            return False
        fast = slow = head
        while True:
            if not (fast.next and fast.next.next and slow.next):
                return False
            fast = fast.next.next
            slow = slow.next

            if fast is slow:
                return True
