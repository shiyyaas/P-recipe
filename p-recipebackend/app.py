from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/hello')
def hello():
    return jsonify({"message": "Hello! Your Recipe API is working! 🍕"})

@app.route('/api/recipes')
def get_recipes():
    recipes = [
        {"id": 1, "title": "Pasta", "cook_time": "15 mins"},
        {"id": 2, "title": "Pizza", "cook_time": "25 mins"}
    ]
    return jsonify(recipes)

if __name__ == '__main__':
    app.run(debug=True)