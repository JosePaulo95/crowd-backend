from flask import Flask
from .routes import configure_routes  # Importa a função para configurar as rotas

def create_app():
    app = Flask(__name__)
    
    configure_routes(app)  # Configura as rotas
    
    return app
