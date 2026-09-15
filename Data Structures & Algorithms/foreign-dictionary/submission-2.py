class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c:set() for word in words for c in word}
        
        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            minLen = min(len(w1),len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                # invalid order
                return ""

            # search until there is a difference
            for j in range(minLen):
                # stablish the lexical order
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break

        visit = {} # False = visited, True = in the current path 
        res = []

        # dfs postorder 
        def dfs(c):
            if c in visit:
                return visit[c]

            visit[c] = True

            for n in adj[c]:
                if dfs(n):
                    return True
                    
            visit[c] = False

            res.append(c)

        for c in adj:
            if dfs(c):
                return ""

        res.reverse()

        return "".join(res)