# O(n) Time Complexity, iterate through each element
# O(1) Space Complexity

class Solution:
    def maxProfit(self, prices):
        # Start and high variables
        buy_price = prices[0]
        profit = 0

        # Start at 2nd elements
        for p in prices[1:]:
            if buy_price > p:
                buy_price = p
            
            profit = max(profit, p - buy_price)
        
        return profit