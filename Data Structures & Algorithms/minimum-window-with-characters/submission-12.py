class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target = Counter(t)
        target = dict(target)
        current = {}
        left = 0
        cumplidos = 0
        min_len = float('inf')
        min_window = [-1,-1]
        
        for right,ch in enumerate(s):
            if cumplidos == len(target):
                while left < right:
                    if s[left] in target:
                        temp = s[left]
                        current[temp] -= 1
                        left += 1
                        if current[temp] < target[temp]:
                            cumplidos -= 1
                            break
                    else:
                        left += 1

                while left < right:
                    if s[left] not in target:
                        left += 1
                    elif (s[left] in target and current[s[left]]-1 >= target[s[left]]):
                        current[s[left]] -= 1
                        left += 1
                    else:
                        break

            if ch in target:
                current[ch] = current.get(ch,0) + 1
                
                if current[ch] == target[ch]:
                    cumplidos += 1

                if cumplidos == len(target) and right - left + 1 < min_len:
                    # verifico que no haya valores basura
                    while left < right and cumplidos == len(target):
                        if s[left] in target and current[s[left]]-1 >= target[s[left]]:
                            current[s[left]] -= 1
                        elif s[left] in target:
                            break
                        left += 1
                    # actualizo la respuesta
                    min_len = right - left + 1
                    min_window = [left,right+1]
                    
                            
            elif ch not in target and left == right:
                left += 1

        

        return s[min_window[0]:min_window[1]]