from flask import Flask
from flask_graphql import GraphQLView

from .api import api
from .forms import *
from .graphql import schema
from .views import frontend


def create_app():
    app = Flask(__name__)
    app.register_blueprint(api)
    app.register_blueprint(frontend)
    app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))
    return app
