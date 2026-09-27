class Solution:
    def isHappy(self, n: int) -> bool:

        seenSums = set() 
        squareSum = 0 

        while True: 
            squareSum = 0
            strNum = str(n)

            for d in strNum:
                d = int(d)
                squareSum += d ** 2

            #number is happy
            if squareSum == 1: 
                return True 
            #we have reached the cycle
            elif squareSum in seenSums:  
                return False 
            else:
                    
                #keep exploring
                seenSums.add(squareSum)
                #reset square sum
                n = squareSum 
        
        return True

            

        