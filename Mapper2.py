import sys

def count_occurrences(data, word):
    count = 0
    for occurrence in data:
        if occurrence.lower() == word.lower():  # Convert both to lowercase for case-insensitive comparison
            count += 1
    return count+2

def mapper(input_data, doc_id, words_in_paragraph):
    # Initialize a dictionary to store term frequency for each document
    term_frequency = {}
    # Process each input tuple
    for item in input_data:
        word_id = item[0]
        word = item[1]
        # Count the occurrences of the word in the paragraph
        count = count_occurrences(words_in_paragraph, word)
        # Append the (word_id, count) tuple to the list
        term_frequency.setdefault(doc_id, []).append((word_id, count))
   
    # Print the document ID and the term frequency for each document
    print(doc_id, end='\t')
    for pair in term_frequency[doc_id]:
        print(f"({pair[0]},{pair[1]})",end=',')
    print()
   

def convert(temp):
    lst = []
    for item in temp:
        # Remove the leading and trailing parentheses
        item = item.strip('()')
        # Split the tuple by comma
        lst.append(item.split(','))
    return lst

if __name__ == '__main__':
    # Read input from file
    input_data = []
    for line in sys.stdin:
        line = line.strip().split('\t')
        line = convert(line)
        input_data.extend(line)
    with open('/home/eman/Downloads/input(1).txt') as file:
        line2 = file.readlines()
        for docs in line2:
            doc_id, text = docs.strip().split('\t')
            text = text.split()
            # Call the mapper function with input_data
            mapper(input_data, doc_id, text)
