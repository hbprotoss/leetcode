#!/usr/bin/env python

__author__ = 'hbprotoss'

"""
https://oj.leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

Best Time to Buy and Sell Stock II

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
"""

class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if len(prices) <= 1:
            return 0

        sum = 0
        i = 0
        while i < len(prices):
            while i < len(prices) - 1 and prices[i] >= prices[i + 1]:
                i += 1
            if i < len(prices) - 1:
                _min = prices[i]
            else:
                break
            while i < len(prices) - 1 and prices[i] <= prices[i + 1]:
                i += 1
            _max = prices[i]

            i += 1
            if i == len(prices) - 1 and prices[i - 1] <= prices[i]:
                _max = prices[i]

            sum += (_max - _min)
        return sum

if __name__ == '__main__':
    s = Solution()
    assert s.maxProfit([1,2,3,4,5,6]) == 5
    assert s.maxProfit([1,2,3,2,3,4]) == 4
    assert s.maxProfit([1,2,3,2,3,4,3]) == 4
    assert s.maxProfit([1,2,3,2,3,4,3,2]) == 4
    assert s.maxProfit([3,2,1,2,3,4,3,4]) == 4
