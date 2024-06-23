from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/portfolio', methods=['GET'])
def get_portfolio():
    portfolio_data = {
        "name": "Gavin Tran",
        "bio": "An avid learner.",
        "projects": [
            {"title": "Project One", "description": "Description of project one.", "link": "#"},
            {"title": "Project Two", "description": "Description of project two.", "link": "#"}
        ]
    }
    return jsonify(portfolio_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
