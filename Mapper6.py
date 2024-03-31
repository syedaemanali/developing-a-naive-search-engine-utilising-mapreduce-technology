#!/usr/bin/env python3

import sys

# Mapper function
def mapper():
    # Input comes from standard input
    for line in sys.stdin:
        # Split the input line into document_id and vector_representation
        document_id, vector_representation = line.strip().split(': ')
        # Emit key-value pairs with document ID and source indicator
        print(f"{document_id}\t{vector_representation}\tRanker")

if __name__ == "__main__":
    mapper()
