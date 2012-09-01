import os
from flask import Flask, request, make_response, render_template
from jinja2.exceptions import TemplateNotFound

app = Flask(__name__)
app.config['DEBUG'] = bool(os.environ.get('DEBUG'))

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    try:
        return render_template(path + '/index.html', path=path)
    except TemplateNotFound as ex:
        return render_template("index.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
