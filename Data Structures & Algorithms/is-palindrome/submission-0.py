class Solution:
    def isPalindrome(self, s: str) -> bool:
        stripped = "".join(char for char in s if char.isalnum()).lower()
        print(stripped)
        print(stripped[::-1])
        return stripped == stripped[::-1]


        