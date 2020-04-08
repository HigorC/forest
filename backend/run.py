from flask import Flask
from backend.routes import routes_blueprint
from backend.assets.banner import banner as banner
import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app = Flask(__name__)
    print(banner)
    print(">> A todo vapor na porta ", port, "\n")
    app.register_blueprint(routes_blueprint)
    app.run(host='0.0.0.0', port=port)
    print("\n>> Fim da linha meu chapa!\n")