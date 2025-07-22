class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        char = set(wordList)

        if endWord not in char:
            return 0

        q = deque()
        q.append((beginWord,1))


        while q :
            beginWord,level = q.popleft()

            for i in range(len(beginWord)):
                
                for c in'abcedfghijklmnopqrstuvwxyz':
                    newWord = beginWord[:i] + c + beginWord[i+1:]

                    if newWord == endWord:
                        return level + 1
                    
                    if newWord in char:
                        q.append((newWord,level+1))
                        char.remove(newWord)
        return 0
        
                    



                


