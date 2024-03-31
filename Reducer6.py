#!/usr/bin/env python3

import sys

# Reducer function
def reducer():
    current_document_id = None
    ranker_values = []
    content_extractor_values = []

    # Input comes from standard input
    for line in sys.stdin:
        # Split the input line into document_id, vector_representation, and source
        document_id, vector_representation, source = line.strip().split('\t')

        # If the document ID changes, process the accumulated values
        if current_document_id != document_id:
            if current_document_id:
                # Emit the processed values for the previous document ID
                emit_values(current_document_id, ranker_values, content_extractor_values)
            # Reset values for the new document ID
            current_document_id = document_id
            ranker_values = []
            content_extractor_values = []

        # Append vector_representation based on source
        if source == 'Ranker':
            ranker_values.append(vector_representation)
        elif source == 'ContentExtractor':
            content_extractor_values.append(vector_representation)

    # Emit the final processed values
    if current_document_id:
        emit_values(current_document_id, ranker_values, content_extractor_values)

def emit_values(document_id, ranker_values, content_extractor_values):
    # Emit the document ID along with its relevant vectors from each source
    print(f"{document_id}\t{'|'.join(ranker_values)}\t{'|'.join(content_extractor_values)}")

if __name__ == "__main__":
    reducer()
