class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.store:
            self.store[key].append((timestamp, value))
        else:
            self.store[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        l = self.store[key]
        if timestamp < l[0][0]:
            return ""
        left, right = 0, len(l) - 1
        while left < right:
            mid = (left + right + 1) // 2
            if l[mid][0] <= timestamp:
                left = mid
            else:
                right = mid - 1
        return l[left][1]