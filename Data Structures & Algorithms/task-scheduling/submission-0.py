class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        frequencies = Counter(tasks)

        max_freq = max(frequencies.values())
        num_max = sum(
            freq == max_freq
            for freq in frequencies.values()
        )

        frame_size = (max_freq - 1) * (n + 1) + num_max

        return max(len(tasks), frame_size)