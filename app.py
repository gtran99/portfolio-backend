from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "https://gtran99.github.io"}})

@app.route('/api/portfolio', methods=['GET'])
def get_portfolio():
    portfolio_data = {
        "name": "Gavin Tran",
        "bio": "An avid learner with 2 years of experience in Software Testing",
        "projects": [
            {"title": "Ecommerce Testing Framework",
             "description": "Developed a test automation suite for an e-commerce website using Python and Flask", 
             "link": "https://github.com/gtran99/Ecommerce-Test"},
            {"title": "Recipe Finder", 
             "description": "A full-stack web application using Flask and the Spoonacular API to find recipes based on selected ingredients", 
             "link": "https://github.com/gtran99/RecipeFinder"}
        ]
    }
    return jsonify(portfolio_data)

if __name__ == '__main__':
    app.run()
