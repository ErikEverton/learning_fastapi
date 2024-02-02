from typing import Annotated

from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.post("/files/")
async def create_file(files: Annotated[list[bytes] | None, File(description="Multiple files as bytes")] = None):
    if not files:
        return {"message": "not file sent"}
    return {"file_size": [len(file) for file in files]}


@app.post("/uploadfiles/")
async def create_upload_file(
    files: Annotated[
        list[UploadFile], File(description="Multiple files as UploadFile")
    ]
):
    if not files:
        return {"message": "No upload file sent"}
    return {"filename": [file.filename for file in files]}


@app.get("/")
async def main():
    content = """
    <body>
        <form action="/files/" enctype="multipart/form-data" method="post">
            <input name="files" type="file" multiple>
            <input type="submit">
        </form>
        <form action="/uploadfiles/" enctype="multipart/form-data" method="post">
            <input name="files" type="file" multiple>
            <input type="submit">
        </form>
    </body>
    """
    return HTMLResponse(content=content)
