from flask import Flask, request, render_template
from search_engine import SearchEngine  # Assume SearchEngine is the above class

app = Flask(__name__)
search_engine = SearchEngine()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('q')
    if query:
        results = search_engine.search(query)
        return render_template('results.html', query=query, results=results)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
