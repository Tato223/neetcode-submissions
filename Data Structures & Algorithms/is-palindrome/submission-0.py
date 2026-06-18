class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        new_str = ""

        for i in s:
            if i.isalnum():
                new_str += i

        if new_str[::-1] == new_str:
            return True
        return False