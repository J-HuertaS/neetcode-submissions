class TimeMap:

    def __init__(self):
        self.mp = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.mp:
            self.mp[key].append((value,timestamp))
        else:
            self.mp[key] = [(value,timestamp)]        

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.mp:
            return ""

        l = 0
        r = len(self.mp[key]) - 1
        ans = -1
        while l <= r:
            m = (r-l)//2 + l
            if self.mp[key][m][1] <= timestamp:
                ans = m
                l = m + 1
            else:
                r = m - 1

        return self.mp[key][ans][0] if ans != -1 else ""

        
