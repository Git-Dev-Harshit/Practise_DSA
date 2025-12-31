class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        max_profit = 0

        for i in range(0, len(prices)):
            for j in range(i+1, len(prices)):
                if prices[i] > prices[j]:
                    continue
                else:
                    if max_profit > abs(prices[i] - prices[j]):
                        continue
                    else:
                        max_profit = abs(prices[i] - prices[j])
                
        return max_profit

# optimized approach
# class Solution(object):
    # def maxProfit(self, prices):
    #     """
    #     :type prices: List[int]
    #     :rtype: int
    #     """
    #     min_price = float('inf')
    #     max_profit = 0
        
    #     for price in prices:
    #         if price < min_price:
    #             min_price = price
    #         else:
    #             max_profit = max(max_profit, price-min_price)
        
    #     return max_profit    

if __name__ == "__main__":
    a = Solution()
    print(a.maxProfit([7,6,5,4,3]))