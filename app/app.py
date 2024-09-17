from flask import Flask
from models.db import initDB
from controllers.UserController import UserController
from tortoise import run_async
app = Flask(__name__)
app.config["DATABASE_URL"] = 'postgres://postgres:1234@localhost:5432/pi'
UserController.init_app(app)

if __name__ == "__main__":
    run_async(initDB.init())
    app.run(port=4000, debug=True)