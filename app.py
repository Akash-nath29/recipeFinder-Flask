from flask import Flask, render_template, request
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = 'MLXH243rjBDIBibiBIbibIUBImmfrdTWS7FDhdwYF56wPj8'
api_key = '21ce19a86415375dd63c0563138cd22a'

# Base URL for Edamam Recipe Search API
base_url = 'https://api.edamam.com/search'

# Function to search for recipes
def search_recipes(query):
    params = {
        'q': query,
        'app_id': '0eae0989',
        'app_key': api_key,
    }

    response = requests.get(base_url, params=params)
    data = response.json()
    return data['hits']  # Return a list of recipe details

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        query = request.form.get('query')
        recipes = search_recipes(query)
        return render_template('index.html', recipes=recipes, query=query)
    return render_template('index.html', recipes=None, query=None)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='80')
