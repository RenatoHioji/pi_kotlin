from tortoise import Tortoise

class initDB:
    @staticmethod
    async def init(db_url, models):
        await Tortoise.init(
            db_url=db_url,
            modules={"models": models}
        )
        await Tortoise.generate_schemas()
