import sys

def mapper(documents):
    # Store unique words from each document
    unique_words_per_doc = {}
    for doc_id, words in documents.items():
        unique_words = list(set(words))
        unique_words_per_doc[doc_id] = unique_words  

    # Count the number of documents in which each term appears
    term_document_counts = {}
    for doc_words in unique_words_per_doc.values():
        for term in doc_words:
            term_document_counts[term] = term_document_counts.get(term, 0) + 1

    # Output IDF values
    idf_values = {term: count for term, count in term_document_counts.items()}
    return idf_values

if __name__=="__main__":
    # Initialize a dictionary to store words for each document
    documents = {}
    for line in sys.stdin:
        sentence_number, words = line.strip().split('\t')
        sentence_number = int(sentence_number)
        words = words.strip().split(',')
        documents[sentence_number] = words

    idf_values = mapper(documents)
   
    # Print IDF values in the specified format
    for term, count in sorted(idf_values.items()):
        if term:
        	print(f"{term},{count})", end=',')

	

