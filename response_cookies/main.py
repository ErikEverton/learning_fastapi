from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()


@app.get("/cookies-and-object/")
def create_cookie():
    content = {"message": "Come to the dark side, we have cookies"}
    response = JSONResponse(content=content)
    response.set_cookie(key="fakesession", value="fake-cookie-session-value")
    return response