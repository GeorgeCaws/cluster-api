# Load libraries
from flask import Flask             # Flask libraries required for API

api = Flask(__name__)

@api.route("/healthcheck", methods = ["GET"])
def health_check():
    return({"alive": True})

# Start app
if __name__ == "__main__":
    api.run(debug = True, host = "0.0.0.0", port = 50)