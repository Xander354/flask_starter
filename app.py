import flask

app = flask.Flask(__name__)

@app.route('/')
def index():
    return flask.send_file('static/index.html')

if __name__ == '__main__':
    app.run()