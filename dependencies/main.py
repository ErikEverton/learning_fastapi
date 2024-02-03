from typing import Annotated

from fastapi import Depends, FastAPI

app = FastAPI()


async def common_parameters(q: str | None = None, skip: int = 0, limit: int = 100):
    return {'q': q, 'skip': skip, 'limit': limit}


commonsDep = Annotated[dict, Depends(common_parameters)]


@app.get("/items/")
async def read_items(commons: commonsDep):
    return commons


@app.get("/users/")
async def read_users(commons: commonsDep):
    return commons
