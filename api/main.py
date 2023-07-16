from fastapi import FastAPI

from ask import ask

app = FastAPI()


@app.get("/")
async def root():
    res = await ask()
    return {"message": "Hello World", "response": res}