class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # split s into a list of words
        words = s.split(" ")

        # we know that if the length is not the same it won't match
        if len(pattern) != len(words):
            return False

        # these are our two dictionaries that we need
        charToWord = {}
        wordToChar = {}

        for c, w in zip(pattern, words):
            # if the c in charToWord does not match the w we put, return false
            if c in charToWord and charToWord[c] != w:
                return False
            
            # if the w in wordToChar does not match the c we put, then we return false
            if w in wordToChar and wordToChar[w] != c:
                return False

            # populate
            charToWord[c] = w
            wordToChar[w] = c
            
        return True