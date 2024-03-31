#!/usr/bin/env python3

import sys

def reducer():
    current_word = None
    current_count = 0
    vocab = {}
    vocab_id = 0
    
    for line in sys.stdin:
        line = line.strip()
        word, count = line.split('\t', 1)
        
        if current_word == word:
            current_count += int(count)
        else:
            if current_word:
                vocab[current_word] = vocab_id
                vocab_id += 1
            current_word = word
            current_count = int(count)
    
    if current_word:
        vocab[current_word] = vocab_id
    
    sorted_vocab = sorted(vocab.items(), key=lambda x: x[1])
    for word, vocab_id in sorted_vocab:
        print(f'({vocab_id}, \'{word}\')')

if __name__ == "__main__":
    reducer()
