class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:

        players.sort()
        trainers.sort()

        l = 0 
        r = 0
        m = len(players)
        n = len(trainers)
        count  = 0

        while(l<m  and r <n ):
            if players[l]<=trainers[r]:
                l = l + 1
            r = r +1
        return l
        