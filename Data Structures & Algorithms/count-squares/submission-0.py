class CountSquares:
    from collections import Counter

    def __init__(self):
        self.points = Counter()

    def add(self, point: List[int]) -> None:
        self.points[(point[0], point[1])] += 1

    def count(self, point: List[int]) -> int:
        res = 0
        for p in self.points:
            if p[0] == point[0] and p[1] != point[1]:
                length = abs(p[1] - point[1])
                if (p[0] - length, p[1]) in self.points and (point[0] - length, point[1]) in self.points:
                    res += self.points[p] * self.points[(p[0] - length, p[1])] * self.points[(point[0] - length, point[1])]
                if (p[0] + length, p[1]) in self.points and (point[0] + length, point[1]) in self.points:
                    res += self.points[p] * self.points[(p[0] + length, p[1])] * self.points[(point[0] + length, point[1])]
        return res
        
