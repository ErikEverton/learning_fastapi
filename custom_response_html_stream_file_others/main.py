from typing import Any

import orjson
from fastapi import FastAPI, Response
from fastapi.responses import (
    FileResponse, HTMLResponse, ORJSONResponse, PlainTextResponse, RedirectResponse, StreamingResponse, UJSONResponse
)

app = FastAPI(
    #default_response_class=ORJSONResponse | FastAPI will use this by default. 
)


@app.get("/items/", response_class=ORJSONResponse)
async def read_items():
    return ORJSONResponse([{"item_id": "Foo"}])


def generate_html_response():
    html_content = """
        <html>
            <head>
                <title>Products</title>
            </head>
            <body>
                <h1>No products for now, thank you for comming.</h1>
            </body>
        </html>
    """
    return HTMLResponse(content=html_content, status_code=200)


@app.get("/products/", response_class=HTMLResponse)
async def read_products():
    return generate_html_response()


@app.get("/legacy/")
def get_legacy_data():
    data =  """<?xml version="1.0"?>
    <shampoo>
        <Header>
            Apply shampoo here.
        </Header>
        <Body>
            You'll have to use soap here.
        </Body>
    </shampoo>
    """

    return Response(content=data, media_type="application/xml")



@app.get("/", response_class=PlainTextResponse)
async def main():
    return "Hello, world"


#ORJSONResponse might be faster
@app.get("/objects/", response_class=UJSONResponse)
async def read_objects():
    return [{"object_id": "bar"}]

@app.get("/typer/", response_class=RedirectResponse, status_code=302)
async def redirect_typer():
    return "https://typer.tiangolo.com"


#if you have a file this really works
file = "something.mp4"


@app.get("/stream/")
async def stream():
    def iterfile():
        with open(file, mode="rb") as file_like:
            yield from file_like
    return StreamingResponse(iterfile(), media_type="video/mp4")


some_file_path = "music.mp3"    

@app.get("/file/", response_class=FileResponse)
async def read_file():
    return some_file_path


class CustomORJSONResponse(Response):
    media_type = "application/json"

    def render(self, content: Any) -> bytes:
        assert orjson is not None, "orjson must be installed" 
        return orjson.dumps(content, option=orjson.OPT_INDENT_2)


@app.get("/custom/", response_class=CustomORJSONResponse)
async def custom():
    return {"message": "Hello World"}
