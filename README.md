# developing-a-naive-search-engine-utilising-mapreduce-technology
https://drive.google.com/file/d/1ysg6mP4ajsLGidT_6jmFq7qXI8Ugxm1r/view?usp=sharing

 
Assignment #2:
 
 
Submitted to:   Ma’am Kainat Iqbal
 
Submitted by:  Syeda Eman Ali (i221936), Vanya Shafiq (i221953), Aliza Saadi (i221871)

Course Name:   Fundamentals of Big Data Analytics
 
Department/section: DS-4A
 
Submission Date: 31/03/24
 
 
 



1st MapReduce Job: Basics of Information Retrieval for Text
Task: Introduce the concept of information retrieval and the Vector Space Model.
Explanation: Describe the fundamental principles of information retrieval, including document representation and relevance calculation using TF/IDF.
2nd MapReduce Job: Term Frequency (TF)
Task: Calculate the term frequency for each term in the documents.
Explanation: Illustrate how documents can be represented using Term Frequency (TF) and discuss the importance of this representation in information retrieval.
3rd MapReduce Job: Inverse Document Frequency (IDF)
Task: Compute the inverse document frequency for each term.
Explanation: Introduce the concept of IDF and demonstrate its calculation based on term occurrences across documents.
TF/IDF Weights
Task: Calculate TF/IDF weights for terms in documents.
Explanation: Explain the computation of TF/IDF weights and their significance in representing term importance in documents.
   4th MapReduce Job: Basic Vector Space Model
Task: Represent documents and queries as vectors using TF/IDF weights.
Explanation: Describe how TF/IDF weights are converted into vector representations and used to compare documents and queries.
5th MapReduce Job: Relevance Score
Task: Calculate relevance score for the query and document.
Explanation: Calculates a relevant score to see how relevant the query is to each document.




6th MapReduce Job: Vocabulary Construction
Task: Construct a vocabulary of unique terms from the document corpus.
Explanation: Detail the creation of a vocabulary data structure that consolidates term information for further processing.




Processing Big-Data using Hadoop Clusters on Azure:

We created 3 Virtual Machines on Azure. One Master and two slaves. Using putty we accessed their terminals on our local machine, and then set-up the hadoop cluster. The nodes were linked using ssh keys. 
We uploaded our codes and data to the master node using scp. The distributed computing helped in processing the Big-Data and allowed us to create a large-scale search engine.

Master Node Details: 
Name: hadoop-master
Ip: 20.11.70.219

Chaining Multiple Map-Reduce:

To allow the multiple map-reduce functions to work together, we created two python scripts; chain.py and chain2.py

chain.py: Runs all map-reduce on data. The output from the former map reduce is formatted and used as input in the next one.

chain2.py: Takes query from user, runs all map-reduce on the query as on the documents. Computes similarity between documents and query. To find similar items.



