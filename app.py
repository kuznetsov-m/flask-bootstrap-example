from flask import Flask, render_template
from sys import argv

app = Flask(__name__)

@app.route('/')
def index():
    posts = []
    return render_template('index.html', posts=posts)

if __name__ == "__main__":
    if len(argv) == 2:
        app.run(host='0.0.0.0', port=int(argv[1]))
    else:
        app.run(port=8080, debug=True) 