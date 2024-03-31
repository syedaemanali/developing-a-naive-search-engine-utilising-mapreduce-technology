import sys

def load_tf_values():
    # Load TF values from the output file
    tf_values = {}
    with open('/home/eman/Downloads/output_TF_reducer.txt', 'r') as f:
        for line in f:
            doc_id, tf_terms = line.strip().split('\t')
            tf_values[int(doc_id)] = eval(tf_terms)  # Convert string representation to tuple
    return tf_values

def reducer(idf_values):
    tf_values = load_tf_values()
   
    # Calculate TF/IDF weights for each document
    tfidf_weights = {}
    for doc_id, tf_terms in tf_values.items():
        doc_weights = []
        # Calculate TF/IDF weight for each term in the document
        for term, tf in tf_terms:
            for idf_term, doc_count in idf_values:
                if int(idf_term) == term:
                    # Divide TF by IDF to get TF/IDF weight
                    tfidf_weight = tf / doc_count
                    doc_weights.append((term, tfidf_weight))
                    break  # Stop searching for IDF value once found
        tfidf_weights[doc_id] = doc_weights

    # Output TF/IDF weights
    for doc_id, weights in sorted(tfidf_weights.items()):
        # Print document ID followed by its corresponding TF/IDF tuples separated by tabs
        print(doc_id, end='\t')
        for term, weight in weights:
            print(f"({term},{weight:.2f})", end=',')  # Format weight to two decimal places
        print()  # Print a new line after each document's weights

if __name__ == "__main__":
    idf_values = []
    for line in sys.stdin:
        # Parse IDF values from input lines
        tokens = line.strip().split(',')
        word_id = tokens[0].strip()[1:]
        count = float(tokens[1].strip()[:-1])
        idf_values.append((int(word_id), count))
   
    reducer(idf_values)
	

