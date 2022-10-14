'Flask on Lambda'
import serverless_wsgi
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/test")
def hello_world():
    'Test Route'
    return render_template('index.html')


def handler(event, context):
    'Handler Function'
    return serverless_wsgi.handle_request(app, event, context)
