from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        
        # DP table to store the maximum profit for each range
        dp = [[0] * n for _ in range(n)]

        # Fill the DP table
        for length in range(2, n + 1):  # length of the interval
            for start_Day in range(n - length + 1):  # starting index of the interval
                end_Day = start_Day + length - 1  # ending index of the interval
                max_Profit = 0  # Initialize maximum profit for this interval
                
                # Iterate over all possible buy days in the current interval
                for buy_Day in range(start_Day, end_Day):
                    # Iterate over all possible sell days after the buy day
                    for sell_Day in range(buy_Day + 1, end_Day + 1):
                        # Calculate profit for this buy-sell pair
                        current_Profit = (prices[sell_Day] - prices[buy_Day] +
                                          (dp[start_Day][buy_Day - 1] if buy_Day > start_Day else 0) +
                                          (dp[sell_Day + 1][end_Day] if sell_Day < end_Day else 0))
                        # Update the max profit for this interval
                        max_Profit = max(max_Profit, current_Profit)

                dp[start_Day][end_Day] = max_Profit  # Store the result in DP table

        return dp[0][n - 1]  # The answer is the maximum profit for the full range

# Time Complexity: O(n^3) - There are three nested loops to fill the DP table.
# Space Complexity: O(n^2) - The DP table stores results for each (start_Day, end_Day) pair.