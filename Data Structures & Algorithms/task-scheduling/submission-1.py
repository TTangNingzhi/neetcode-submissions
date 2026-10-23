from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        max_freq = max(counts.values())
        n_tasks_max_freq = len([v for v in counts.values() if v == max_freq])
        return max(len(tasks), (max_freq - 1) * (n + 1) + n_tasks_max_freq)