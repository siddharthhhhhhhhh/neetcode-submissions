class Solution:

    def encode(self, strs: List[str]) -> str:
        str1 = ""
        for i in strs:
            str1 += i + "P"
        return str1
    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return []
        list1 = s[:-1].split("P")
        return list1