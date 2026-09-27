class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        #[1,2,4,2,3,5,3,4],
        #[1,2,2,3,3,4,4,5]

        if len(hand) % groupSize:
            return False
        
        freqs = Counter(hand)
        hand.sort()
        
        for num in hand:
            if freqs[num]:
                for i in range(num, num + groupSize):
                    if not freqs[i]:
                        return False
                    freqs[i] -= 1
        
        return True