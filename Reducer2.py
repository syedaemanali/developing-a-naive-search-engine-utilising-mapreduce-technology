import sys
from collections import defaultdict
import re

# Function to process the input data and print the reduced output
def reducer():
    current_doc = None  # Keep track of the current document ID
    doc_data = defaultdict(list)  
   
    for line in sys.stdin:
        line = line.strip()  

        # Split each line into document ID and content
        doc_id, content = line.split('\t', 1)
        doc_id = int(doc_id)  # Convert document ID to integer

        # Check if it's a new document
        if current_doc is not None and doc_id != current_doc:
            # Print the data for the previous document
            print_doc_data(current_doc, doc_data[current_doc])
            # Clear data for the previous document
            doc_data[current_doc].clear()

        # Update the current document ID
        current_doc = doc_id
        # Extract word-count pairs using regular expression
        pairs = re.findall(r'\((\d+),(\d+)\)', content)
        # Process each word-count pair
        for pair in pairs:
            # Convert word ID and count to integers
            word_id, count = map(int, pair)
            # Add word-count pair to document data
            doc_data[doc_id].append((word_id, count))

    # Print the data for the last document
    if current_doc is not None:
        print_doc_data(current_doc, doc_data[current_doc])

# Function to print document data, filtering out tuples with count > 0
def print_doc_data(doc_id, data):
    # Filter out tuples where count > 0 for each list of tuples in data
    filtered_data = [(word_id, count) for word_id, count in data if count > 0]
   
    if filtered_data:
        print(doc_id, end='\t')
        for word_id, count in filtered_data:
            print(f"({word_id},{count})", end=',')
        print()

# Entry point of the program
if __name__ == '__main__':
    reducer()

	

