#!/usr/bin/env python3
import sys

def mapper():
    for line in sys.stdin:
        data = line.strip().split(': ')
        doc_id = data[0]
        shingle_weight_pairs = eval(data[1])
        for shingle, weight in shingle_weight_pairs:
            print(f"{shingle}\t{weight}\t{doc_id}")

if __name__ == "__main__":
    mapper()
