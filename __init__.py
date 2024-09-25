from flask_restx import Namespace, Resource, Api
from flask import session, Blueprint

csrf_namespace = Namespace('csrf', description="Endpoint to get the current CSRF token")

@csrf_namespace.route('')
class CSRFToken(Resource):
    def get(self):
        return {
            "csrf_token": session.get("nonce")
        }

def load(app):
    api = Blueprint("csrf_api", __name__, url_prefix="/api/v1")
    CSRF_API_v1 = Api(api, version="v1", doc=app.config.get("SWAGGER_UI"))
    CSRF_API_v1.add_namespace(csrf_namespace, "/csrf_token")
    app.register_blueprint(api)