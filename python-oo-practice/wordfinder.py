"""Word Finder: finds random words from a dictionary."""

import random


class WordFinder:
    def __init__(self, file):
        self.file = file
        self.words = []
        self.load()

    def load(self):
        items = open(self.file, 'r')
        for item in items:
            self.words.append(item)

        print(f"{len(self.words)} words read")

    def random(self):
        return random.choice(self.words)
