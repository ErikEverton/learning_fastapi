from fastapi import FastAPI

app = FastAPI()

@app.route('/')
async def root():
    return {"message": "Hello world!"}
