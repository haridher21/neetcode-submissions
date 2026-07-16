class TimeMap:

    def __init__(self):
        self.keys = {}
        self.timestamps = {} 

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.keys:
            self.keys[key].append([timestamp, value])
        else:
            self.keys[key] = [[timestamp, value]]
        

    def get(self, key: str, timestamp: int) -> str:
        if key in self.keys:
            l, r = 0, len(self.keys[key]) - 1
            while l <= r:
                mid = l + ((r - l) // 2)
                if self.keys[key][mid][0] > timestamp:
                    r = mid - 1
                elif self.keys[key][mid][0] < timestamp:
                    l = mid + 1
                else:
                    return self.keys[key][mid][1]
            if r < 0:
                return ""
            return self.keys[key][r][1]
        return ""
