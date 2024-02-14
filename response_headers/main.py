from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()


@app.get("/headers-and-object/")
def get_headers():
    content = {"message": "Hello World"}
    headers = {"X-Cat-Dog": "alone in the world"}
    return JSONResponse(content=content, headers=headers)
 
