class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        cars = [(position[i], speed[i]) for i in range(n)]
        cars.sort(key=lambda c: c[0])
        fleets = 0
        while cars:
            top = cars.pop()
            fleets += 1
            while cars:
                cur = cars.pop()
                if cur[1] > top[1]:
                    meet_pos = (top[0] - cur[0]) / (cur[1] - top[1]) * cur[1] + cur[0]
                    if meet_pos <= target:
                        continue
                cars.append(cur)
                break
        return fleets
