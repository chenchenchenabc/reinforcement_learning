from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_grid/<int:n>')
def generate_grid(n):
    if 5 <= n <= 9:
        grid = [[0 for _ in range(n)] for _ in range(n)]  # 0 表示空單元格
        return jsonify(grid)
    return jsonify({'error': 'Invalid grid size'})

if __name__ == "__main__":
    app.run(debug=True)
