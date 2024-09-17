from tortoise import Tortoise
class initDB():
    async def init():
        await Tortoise.init(
            db_url = app.config['DATABASE_URL'],
            modules = {
                "models": ['models.User']
            }
        )
        