from flask import Flask
from blueprint.main import route
from blueprint.api import api

# Example Profile Class
class profile:
    def __init__(self, user:str, description: str):
        self.user = user
        self.description = description

# Main
PORT = 10008

app = Flask(__name__)

# blueprints
app.register_blueprint(route)
app.register_blueprint(api, url_prefix='/api')

if __name__ == "__main__": app.run("0.0.0.0", PORT, debug=False)