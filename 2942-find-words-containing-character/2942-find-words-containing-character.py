class Solution:
    def findWordsContaining(self, words, x):
        """
        Idea:
        - Traverse each word with its index.
        - Check whether character x exists in the word.
        - If found, add the word's index to the answer.

        Example:
        words = ["abc", "bcd", "aaaa", "cbc"], x = "a"

        "abc"   -> contains "a" -> index 0
        "bcd"   -> doesn't contain "a"
        "aaaa"  -> contains "a" -> index 2
        "cbc"   -> doesn't contain "a"

        Answer = [0, 2]

        Time Complexity: O(n * m)
        - n = number of words
        - m = maximum length of a word

        Space Complexity: O(k)
        - k = number of matching words
        """

        ans = []

        for i in range(len(words)):
            if x in words[i]:
                ans.append(i)

        return ans