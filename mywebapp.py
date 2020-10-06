import flask

app = flask.Flask("mywebapp")

@app.route("/")
def indexpage():
    return "Wel Come"

if __name__ == "__main__":
    app.run()