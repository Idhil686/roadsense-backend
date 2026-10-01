from flask import Flask
from flask_cors import CORS

from routes.main_routes import main_bp
from routes.predict_routes import predict_bp


def create_app():
    app = Flask(__name__, template_folder='templates', static_folder='static')
    CORS(app)

    app.register_blueprint(main_bp)
    app.register_blueprint(predict_bp)

    return app


app = create_app()

if __name__ == '__main__':
    app.run(debug=True, port=5000, use_reloader=False)
