from flask import Flask
from flask_cors import CORS


# Instantiate flask application
app = Flask(__name__)


# Update application constantly
app.config.from_object(__name__)


# Enable Cross origin resource sharing
CORS(app, resource={r"/*": {
    'origins': "http://localhost:8080",  # default port for vue
    "allow_headers": "Access-Control-Allow-Origin"
    }
})


@app.route("/", methods=["GET"])
def greetings():
    return "hello hello"


if __name__ == "__main__":
    app.run(debug=True)
