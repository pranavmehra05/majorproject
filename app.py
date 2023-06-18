from flask import Flask, render_template, request
from search import perform_search

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    search_query = request.form['search_query']

    results = perform_search(search_query)

    return render_template('search.html', query=search_query, results=results)

if __name__ == '__main__':
    app.run(port=8000,debug=True) 
    

