from flask import Flask
from controllers.UserController import UserController
from tortoise import run_async
from models.db import initDB 

app = Flask(__name__)
app.config["DATABASE_URL"] = 'postgres://postgres:1234@localhost:5432/pi'
UserController.init_app(app)

async def setup():
    await initDB.init(
        db_url=app.config['DATABASE_URL'],
        models=['models.User']
    )
    
@app.before_first_request
def before_first_request():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(setup())

if __name__ == "__main__":
    run_async(initDB.init("postgres://postgres:1234@localhost:5432/pi", ))
    app.run(port=4000, debug=True)