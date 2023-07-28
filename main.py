import os

import uvicorn
from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

app = FastAPI(
    title="Syukurin",
    description="A new digital invitation."
)


register_tortoise(
    app,
    db_url=os.environ.get("DB_URL", "sqlite://db.sqlite3"),
    modules={"models": ["models.base", "models.wedding"]},
    generate_schemas=True,
    add_exception_handlers=True,
)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    uvicorn.run("main:app", host="0.0.0.0", port=port, workers=1)
