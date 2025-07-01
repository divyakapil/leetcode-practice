class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # scan left -> right
        # keep track of min_price
        # calculate profit at each step
        # update max_profit

        min_price = float('inf')
        maxProfit = 0

        for current_price in prices:
            if current_price < min_price:
                min_price = current_price # better day to buy
            else:
                profit = current_price - min_price # need to calculate profit for each day
                maxProfit = max(maxProfit, profit)

        return maxProfit
