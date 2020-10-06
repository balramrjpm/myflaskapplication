import flask

app = flask.Flask("mywebapp")

@app.route("/")
def indexpage():
    return "Hello World"

if __name__ == "__main__":
    app.run()