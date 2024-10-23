import os
from collections import defaultdict
import re

class Indexer:
    def __init__(self):
        self.index = defaultdict(list)  # word -> list of documents

    def tokenize(self, text):
        # Simple tokenizer: lowercase and split by non-alphabetic characters
        return re.findall(r'\b\w+\b', text.lower())

    def index_document(self, doc_id, text):
        words = self.tokenize(text)
        for word in words:
            if doc_id not in self.index[word]:
                self.index[word].append(doc_id)

    def build_index(self, data_dir='crawled_data'):
        # Iterate through all crawled documents
        for filename in os.listdir(data_dir):
            if filename.endswith(".txt"):
                filepath = os.path.join(data_dir, filename)
                with open(filepath, 'r', encoding='utf-8') as f:
                    text = f.read()
                    self.index_document(filepath, text)

    def save_index(self, file='index.txt'):
        with open(file, 'w') as f:
            for word, doc_list in self.index.items():
                f.write(f'{word}: {",".join(doc_list)}\n')

# Create and build the index
indexer = Indexer()
indexer.build_index()
indexer.save_index()
