class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:

        players.sort()
        trainers.sort()

        l = 0 
        r = 0
        m = len(players)
        n = len(trainers)
        count  = 0

        while(l<n  and r <m ):
            if trainers[l]>=players[r]:
                r = r +1
            l = l + 1
        return r
        