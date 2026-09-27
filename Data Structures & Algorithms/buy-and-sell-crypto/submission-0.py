class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        currMin = prices[0]
        ans = 0

        for i in range(1,len(prices)):
            if currMin > prices[i]:
                currMin = prices[i]
            else: 
                ans = max(ans, prices[i] - currMin)
        
        return ans 
                
        