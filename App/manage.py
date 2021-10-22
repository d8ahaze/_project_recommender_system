from fastapi import FastAPI

app = FastAPI()


# python -m uvicorn app.manage:app --port 8000 --reload

@app.post("/")
async def json():
    return {"value:", "nothing"}
