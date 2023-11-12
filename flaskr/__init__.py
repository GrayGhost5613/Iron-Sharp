import os
from . import db
from flask import Flask
def create_app():
    app = ...
    # existing code omitted

    
    db.init_app(app)

    return app