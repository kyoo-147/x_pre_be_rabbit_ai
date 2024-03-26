from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Truyền danh sách các chữ cái cho Jinja2
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    return render_template('index.html', alphabet=alphabet)

if __name__ == '__main__':
    app.run(debug=True)
