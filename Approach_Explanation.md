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

        # Time Complexity: O(n^3) - There are nested loops for buy/sell combinations and recursive calls.
        # Space Complexity: O(n) - The recursion stack can go as deep as n in the worst case.
        ```
    <hr>

- ## Solution 2: Using Memoization
    - ### Intuition
        - The goal is to maximize profit from buying and selling stocks based on given daily prices. The approach uses recursion to explore all possible buy-sell pairs while considering profits from earlier and later transactions.

    - ### Approach
        1. **Recursive Function**: The function `find_Max_Profit_Between_Range` computes the maximum profit for a specified range of days.
        2. **Base Case**: If the starting day is greater than the ending day, it returns 0 (no profit).
        3. **Memoization**: A dictionary `profit_Cache` is used to store already computed results for specific ranges, avoiding redundant calculations.
        4. **Nested Loops**: 
            - For each possible buy day, iterate over all possible sell days after that buy day.
            - Calculate the profit for each buy-sell combination, including profits from previous and subsequent days.
        5. **Max Profit Calculation**: Update the maximum profit for the current range.

    - ### Time Complexity
        - **O(n²)**: The time complexity arises from the nested loops for buy/sell combinations, while memoization optimizes the number of calculations.

    - ### Space Complexity
        - **O(n²)**: The memoization cache can store results for each combination of start and end days, leading to potentially \(O(n^2)\) entries.


    - ### Code
        ```python
        from typing import List

        class Solution:
            def maxProfit(self, prices: List[int]) -> int:
                profit_Cache = {}

                # Helper function to find the maximum profit within a given range
                def find_Max_Profit_Between_Range(start_Day: int, end_Day: int) -> int:
                    # Base case: if the start day is greater than the end day, no profit can be made
                    if start_Day > end_Day:
                        return 0

                    if (start_Day, end_Day) in profit_Cache:
                        return profit_Cache[(start_Day, end_Day)]
                    
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

                    profit_Cache[(start_Day, end_Day)] = max_Profit
                    return max_Profit  # Return the maximum profit found in this range
                
                # Start the recursive profit calculation from the full range of days
                return find_Max_Profit_Between_Range(0, len(prices) - 1)
        ```
    <hr>

- ## Solution 3: Using Dynamic Programming

    - ### Intuition
        - The goal is to maximize profit from buying and selling stocks over a range of days. By using a dynamic programming (DP) approach, we can systematically calculate the maximum profit for various intervals, storing results to avoid redundant calculations.

    - ### Approach
        1. **DP Table**: We create a 2D DP table where `dp[i][j]` represents the maximum profit obtainable from the interval starting at day `i` and ending at day `j`.
        2. **Filling the DP Table**:
            - We iterate over increasing lengths of intervals (from 2 to `n`).
            - For each interval defined by `start_Day` and `end_Day`, we initialize `max_Profit` to 0.
            - We check every possible buy day within the interval, followed by every possible sell day after the buy day.
            - For each buy-sell pair, we calculate the profit and add profits from any previous or subsequent intervals using the values stored in the DP table.
        3. **Result**: The final maximum profit for the entire range is found in `dp[0][n - 1]`.

    - ### Time Complexity
        - **O(n³)**: The complexity arises from three nested loops—one for the interval length, one for the starting day, and one for the buy-sell combinations.

    - ### Space Complexity
        - **O(n²)**: The DP table stores results for each possible `(start_Day, end_Day)` pair, leading to a quadratic space requirement.

    - ### Code
        ```python
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
        ```
    <hr>

- ## Solution 4: Greedy Approach
    - ### Intuition
        - The objective is to maximize profit from stock trading by buying on one day and selling on another. This approach focuses on capturing every upward movement in stock prices.

    - ### Approach
        1. **Initialization**: Start with a variable `profit` set to 0, which will accumulate the total profit.
        2. **Iterate Through Prices**:
            - Loop through the prices starting from the second day.
            - If the price on the current day is greater than the price on the previous day, a profit can be realized by buying on the previous day and selling on the current day.
            - Add the difference (profit) to the total profit.
        3. **Result**: Return the total accumulated profit after iterating through the list.

    - ### Time Complexity
        - **O(n)**: The algorithm traverses the list of prices once, where \(n\) is the number of days.

    - ### Space Complexity
        - **O(1)**: Only a constant amount of space is used for the `profit` variable.

    - ### Code
        ```python
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
        ```