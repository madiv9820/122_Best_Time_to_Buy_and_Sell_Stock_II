from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Helper function to find the maximum profit within a given range
        def find_Max_Profit_Between_Range(start_Day: int, end_Day: int) -> int:
            # Base case: if the start day is greater than the end day, no profit can be made
            if start_Day > end_Day:
                return 0
            
            max_Profit = 0  # Initialize maximum profit for the current range

            # Iterate over all possible buy days
            for buy_Day in range(start_Day, end_Day):
                # Iterate over all possible sell days after the buy day
                for sell_Day in range(buy_Day + 1, end_Day + 1):
                    # Calculate current profit from this buy-sell pair
                    current_Profit = ((prices[sell_Day] - prices[buy_Day]) + 
                                      find_Max_Profit_Between_Range(start_Day, buy_Day - 1) + 
                                      find_Max_Profit_Between_Range(sell_Day + 1, end_Day))
                    
                    # Update max profit if the current profit is greater
                    max_Profit = max(max_Profit, current_Profit)
            
            return max_Profit  # Return the maximum profit found in this range
        
        # Start the recursive profit calculation from the full range of days
        return find_Max_Profit_Between_Range(0, len(prices) - 1)

# Time Complexity: O(n^3) - There are nested loops for buy/sell combinations and recursive calls.
# Space Complexity: O(n) - The recursion stack can go as deep as n in the worst case.