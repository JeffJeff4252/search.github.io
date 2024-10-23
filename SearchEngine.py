import math

class SearchEngine:
    def __init__(self, index_file='index.txt'):
        self.index = self.load_index(index_file)
        self.total_docs = len(self.index)

    def load_index(self, file):
        index = defaultdict(list)
        with open(file, 'r') as f:
            for line in f:
                word, docs = line.strip().split(':')
                index[word] = docs.split(',')
        return index

    def search(self, query):
        query_words = query.lower().split()
        scores = defaultdict(float)

        for word in query_words:
            if word in self.index:
                doc_list = self.index[word]
                idf = math.log(self.total_docs / len(doc_list))
                for doc in doc_list:
                    scores[doc] += 1 * idf  # Basic TF * IDF

        # Sort documents by score
        ranked_docs = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        return ranked_docs

# Create a search engine
search_engine = SearchEngine()

# Query the engine
results = search_engine.search("sample query")
for doc, score in results:
    print(f'Document: {doc}, Score: {score}')
