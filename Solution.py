from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0  # Initialize total profit

        # Iterate through the prices starting from the second day
        for current_Day in range(1, len(prices)):
            # If the price today is greater than the price yesterday,
            # we can realize a profit by buying yesterday and selling today
            if prices[current_Day] > prices[current_Day - 1]:
                profit += (prices[current_Day] - prices[current_Day - 1])  # Add profit to total

        return profit  # Return the total profit

# Time Complexity: O(n) - We traverse the list of prices once.
# Space Complexity: O(1) - We use a constant amount of space for the profit variable.