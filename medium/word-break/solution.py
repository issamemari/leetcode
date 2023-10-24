from typing import List

alphabet = "abcdefghijklmnopqrstuvwxyz"


class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = [None for _ in range(len(alphabet))]


class Solution:
    def __init__(self):
        self.memory = {}

    def buildTrie(self, wordDict: List[str]) -> TrieNode:
        self.root = TrieNode()
        for word in wordDict:
            self.insertWord(word)

    def insertWord(self, word):
        current_node = self.root
        for c in word:
            if current_node.children[ord(c) - ord("a")] is None:
                current_node.children[ord(c) - ord("a")] = TrieNode()

            current_node = current_node.children[ord(c) - ord("a")]

        current_node.is_word = True
        return current_node

    def getSuffixes(self, s: str) -> List[str]:
        suffixes = []
        current_node = self.root

        for i, c in enumerate(s):
            if current_node.children[ord(c) - ord("a")] is None:
                break

            current_node = current_node.children[ord(c) - ord("a")]
            if current_node.is_word:
                suffixes.append(s[i + 1 :])

        return suffixes

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if s in self.memory:
            return self.memory[s]

        self.buildTrie(wordDict)

        suffixes = self.getSuffixes(s)
        if len(suffixes) == 0:
            self.memory[s] = False
            return False

        for suffix in suffixes:
            if suffix == "":
                self.memory[s] = True
                return True

            if self.wordBreak(suffix, wordDict):
                self.memory[s] = True
                return True

        self.memory[s] = False
        return False
