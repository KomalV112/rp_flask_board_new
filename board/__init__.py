import os
from dotenv import load_dotenv
from flask import Flask
from board import pages,posts,database

load_dotenv()


def create_app():
    app=Flask (__name__)
    app.config.from_prefixed_env()

    database.init_app(app)
    app.register_blueprint(pages.bp)
    app.register_blueprint(posts.bp)
    print(f"Current Enviornment:{os.getenv('ENVIORNMENT')}")
    print(f"Database Path:{app.config.get('DATABASE')}")
    return app

