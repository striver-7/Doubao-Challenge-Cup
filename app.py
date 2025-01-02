from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/2048')
def game_2048():
    return render_template('2048.html')

@app.route('/snake')
def game_snake():
    return render_template('snake.html')

@app.route('/sokoban')
def game_sokoban():
    return render_template('sokoban.html')

if __name__ == '__main__':
    app.run(debug=True)
