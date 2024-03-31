#!/usr/bin/env python3

import sys

def mapper():
    for line in sys.stdin:
        line = line.strip()
        words = line.split()
        for word in words:
            print(word.lower() + '\t1')

if __name__ == "__main__":
    mapper()


