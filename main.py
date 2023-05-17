from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

app = FastAPI(title="Tortoise ORM FastAPI example")


register_tortoise(
    app,
    db_url="sqlite://db.sqlite3",
    modules={"models": ["models.wedding"]},
    generate_schemas=True,
    add_exception_handlers=True,
)
