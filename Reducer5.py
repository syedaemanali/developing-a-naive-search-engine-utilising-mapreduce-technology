import sys

current_term = None
doc_vector = {}
query_vector = {}
relevance = 0.0

# Read input from standard input
for line in sys.stdin:
    # Split the input into term, document/query identifier, and term value
    doc_id, term = line.strip().split('\t')
    term_value = term[5:-2]
    term_id = term[0]
   
    # Convert term value to float
    term_value = float(term_value)
   
    # If the term changes, compute relevance and emit the result
    if current_term != term_id:
        if current_term:
            relevance = sum(query_vector.get(term_id, 0) * doc_vector.get(term_id, 0) for term_id in set(query_vector.keys()) & set(doc_vector.keys()))
            print(f"{current_term}\t{relevance}")
       
        # Reset variables for the new term
        current_term = term_id
        doc_vector = {}
        query_vector = {}
   
    # Store term values for documents and queries
    doc_vector[doc_id] = term_value

# Compute relevance for the last term
if current_term:
    relevance = sum(query_vector.get(term_id, 0) * doc_vector.get(term_id, 0) for term_id in set(query_vector.keys()) & set(doc_vector.keys()))
    print(f"{current_term}\t{relevance}")
	

