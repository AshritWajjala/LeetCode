class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy_price = prices[0]
        profit = 0

        for daily_price in prices:
            if buy_price > daily_price:
                buy_price = daily_price
            if profit < daily_price - buy_price:
                profit = daily_price - buy_price
        
        return profit

stock_prices = [7, 6, 5, 4, 3, 2]
sample_obj = Solution()
profit = sample_obj.maxProfit(stock_prices)
print(f"Maximum Profit: {profit}")


