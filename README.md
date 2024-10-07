# 122. Best Time to Buy and Sell Stock II

__Type:__ Medium <br>
__Topics:__ Array, Dynamic Programming, Greedy <br>
__Companies:__ Amazon, Google, Bloomberg, Microsoft, Apple, TikTok, Goldman Sachs, CTC, Meta, Walmart Labs, Adobe, Uber, Citadel, Yahoo, tcs, Zoho, DE Shaw, Yandex, Media.net, Salesforce <br>
__Leetcode Link:__ [Best Time to Buy and Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/)
<hr>

You are given an integer array `prices` where `prices[i]` is the price of a given stock on the <code>i<sup>th</sup></code> day. <br><br>
On each day, you may decide to buy and/or sell the stock. You can only hold __at most one__ share of the stock at any time. However, you can buy it then immediately sell it on the __same day__.<br><br>
Find and _return the __maximum__ profit you can achieve_.
<hr>

### Examples

__Example 1:__ <br>
__Input:__ prices = [7,1,5,3,6,4] <br>
__Output:__ 7 <br>
__Explanation:__ Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4. <br>
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3. <br>
Total profit is 4 + 3 = 7. <br>

__Example 2:__ <br>
__Input:__ prices = [1,2,3,4,5] <br>
__Output:__ 4 <br>
__Explanation:__ Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4. <br>
Total profit is 4.

__Example 3:__ <br>
__Input:__ prices = [7,6,4,3,1] <br>
__Output:__ 0 <br>
__Explanation:__ There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.
<hr>

### Constraints:

- <code>1 <= prices.length <= 3 * 10<sup>4</sup></code>
- <code>0 <= prices[i] <= 10<sup>4</sup></code>