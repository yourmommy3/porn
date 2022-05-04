from flask import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/sender',methods=["GET","POST"])
def sender():
    if request.method == 'POST':
        return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)