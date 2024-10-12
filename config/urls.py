from typing import Union
from fastapi import FastAPI
from routers.post import router as PostRouter
from routers.category import router as CategoryRouter

app = FastAPI(title="FastAPI & AbarORM")


app.include_router(CategoryRouter, prefix="/categories", tags=['categories'])
app.include_router(PostRouter, prefix="/posts", tags=['posts'])
