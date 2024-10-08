# Maximum Profit from Stock Prices: Approaches and Implementations
- ## Solution 1 - Using Recursion
    - ### Intuition
    The goal is to maximize profit from buying and selling stocks given daily prices. The approach explores all possible buy-sell pairs while also considering potential profits from previous and subsequent days.

    - ### Approach
        1. **Recursive Function**: The function `find_Max_Profit_Between_Range` takes a range of days (start and end) and calculates the maximum profit for that range.
        2. **Base Case**: If the starting day is greater than the ending day, no profit can be made, and it returns 0.
        3. **Nested Loops**: 
            - Iterate over all possible buy days.
            - For each buy day, iterate over all possible sell days that come after the buy day.
            - Calculate the profit for each buy-sell pair, adding profits from potential earlier and later transactions (using recursive calls).
        4. **Max Profit Calculation**: Keep track of the maximum profit found for the given range.

    - ### Time Complexity
        - **O(n³)**: The nested loops for all buy/sell combinations and the recursive calls for each transaction lead to a cubic time complexity.

    - ### Space Complexity
        - **O(n)**: The recursion stack can go as deep as the number of days (n) in the worst case.

    - ### Code
        ```python
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
        ```