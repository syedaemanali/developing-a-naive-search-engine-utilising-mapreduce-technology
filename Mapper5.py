import sys

# Read input from standard input
for line in sys.stdin:
    parts = line.strip().split('\t')
    doc_id = parts[0]
    vector_str = parts[1:]
   
    # Remove parentheses from the vector string
    #vector_str = vector_str.strip('()')
    # Emit key-value pairs for each term in the vector
    for term in vector_str:
        #term_id=term[1]
        term_value =term[0:]
        print(f"{doc_id}\t{term_value}")
