
#-------------------------------------------------------------------------
# AUTHOR: Eduardo Castro Becerra 
# FILENAME: indexing.py
# SPECIFICATION: Calculation of the tf-idf of words after removing stop words and stemming 
# FOR: CS 4250- Assignment #1
# TIME SPENT: 1 hour and about 32 minutes 
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH
#AS numpy OR pandas. You have to work here only with standard arrays
# Importing some Python libraries
import csv
import math

#read CSV file 
def read_documents(filename):
    with open(filename, 'r') as csvfile:
        return [row[0] for i, row in enumerate(csv.reader(csvfile)) if i > 0]

#prep terms 
def preprocess_documents(documents, stopwords, stemming_rules):
    terms = set()
    for doc in documents:
        for word in doc.lower().split():
            if word not in stopwords:
                terms.add(stemming_rules.get(word, word))
    return sorted(terms)

#calculate tf
def calculate_tf(term, doc):
    return doc.lower().split().count(term.lower())

#calculate idf
def calculate_idf(term, documents):
    num_docs_with_term = sum(term in doc.lower().split() for doc in documents)
    return math.log(len(documents) / (1 + num_docs_with_term))

#document term matrix 
def build_doc_term_matrix(documents, terms):
    return [[calculate_tf(term, doc) * calculate_idf(term, documents) for term in terms] for doc in documents]

# Main program
if __name__ == "__main__":
    documents = read_documents('collection.csv')

    #stop words and stemming dictionary
    stopwords = {'i', 'and', 'she', 'her', 'they', 'their', 'and'}

    stemming = {'loves': 'love', 'cats': 'cat', 'dogs': 'dog'}

    #get unique terms 
    terms = preprocess_documents(documents, stopwords, stemming)

    #build document term matrix call
    docTermMatrix = build_doc_term_matrix(documents, terms)

    #print table and values
    print("Index Terms:", terms)
    for row in docTermMatrix:
        print(row)