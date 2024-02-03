from fastapi import Depends, FastAPI, Header, HTTPException
from typing_extensions import Annotated

app = FastAPI()


async def verify_token(x_token: Annotated[str, Header()]):
    if x_token != "fake-super-secret_token":
        raise HTTPException(status_code=400, detail="X-token header invalid")
    


async def veirfy_key(x_key: Annotated[str, Header()]):
    if x_key != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-key header invalid")
    return x_key


@app.get("/items/", dependencies=[Depends(verify_token), Depends(veirfy_key)])
async def read_items():
    return [{"item": "foo"}, {"item": "bar"}]

