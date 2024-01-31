from typing import Annotated
from fastapi import FastAPI, Query

app = FastAPI()


@app.get('/items/')
async def read_items(
    q: Annotated[
        str | None, Query(
            title="Query string",
            description="Query string for the items to search in the database that have a good match",
            alias="item-query",
            min_length=3,
            max_length=50,
            pattern="^fixedquery$",
            deprecated=True,
            include_in_schema=False,
        ),
    ] = None
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
