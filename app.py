import os
from flask import Flask, request, make_response, render_template
import web

app = Flask(__name__)
app.config['DEBUG'] = bool(os.environ.get('DEBUG'))

@app.route("/")
def index():
    name = request.form.get("name", "world")
    return render_template("index.html", name=name)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
