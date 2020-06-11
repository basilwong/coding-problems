import collections

class Solution:
    def breadth_first_search(self, order):

        decrypted = collections.deque()
        queue = collections.deque()
        visited = set()
        temp = collections.deque()

        for letter in order:
            for i in range()

    def decrypt_to_map(self, words):
        """
        Creates adjacency matrix for the letters within the words. If a letter is
        in the value of a key, then that letter comes after that word.
        """
        order = dict()
        j = 0
        max_length = max(len(w) for w in words)
        while j < max_length:
            for i in range(len(words)):
              if j >= len(words[i]) or j >= len(words[i + 1]):
                  continue
              if words[i][j] == words[i + 1][j]:
                  continue
              if words[i][j] in order:
                  order[words[i][j]].add(words[i + 1][j])
              else:
                  order[words[i][j]] = {words[i  + 1][j]}
        return order

    def alienOrder(self, words: List[str]) -> str:

        if not words:
            return list()
