#!/usr/bin/env python3
import sys

def reducer():
    vocabulary=['a', 'according', 'at', 'august', 'bright', 'by', 'census', 'day', 'end',
    'fallen', 'how', 'i', 'is', 'it', 'i’ve', 'latest', 'many', 'miles',
    'million', 'more', 'moscow', 'of', 'population', 'than', 'the', 'this',
    'time', 'to', 'two', 'warm', 'was', 'wonder', 'or', 'not', 'be']
    vector_length = None
    vocab_length=len(vocabulary)
    vector = [0] * vocab_length # Assuming 34 shingles
    
    for line in sys.stdin:
        shingle_index, weight, doc_id = line.strip().split('\t')
        shingle_index = int(shingle_index)
        weight = float(weight)
        
        if vector_length is None:
            vector_length = shingle_index
        
        if shingle_index == 0:
            continue
        
        vector[shingle_index - 1] = weight
    
    # Print the vector
    print(vector)

if __name__ == "__main__":
    reducer()

