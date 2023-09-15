# https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-iii/

def maxProfit(prices):
    buy1, buy2 = -prices[0], -prices[0]
    sell1, sell2 = 0, 0
    for i in range(len(prices)):
        buy1 = max(buy1, -prices[i])
        sell1 = max(sell1, buy1 + prices[i])
        buy2 = max(buy2, sell1 - prices[i])
        sell2 = max(sell2, buy2 + prices[i])
    return sell2

if __name__ == "__main__":
    prices = [3,3,5,0,0,3,1,4]
    print(maxProfit(prices))