class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        required = {}
        window = {}

        for char in s1:
            required[char] = required.get(char, 0) + 1

        window_size = len(s1)

        for right, char in enumerate(s2):
            window[char] = window.get(char, 0) + 1

            if right >= window_size:
                left_char = s2[right - window_size]
                window[left_char] -= 1

                if window[left_char] == 0:
                    del window[left_char]

            if window == required:
                return True

        return False