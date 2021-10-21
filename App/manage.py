from fastapi import FastAPI

app = FastAPI
# python -m uvicorn -r app.manage:app --port 8000

@app.post("/")
async def json():
    return {"Value": "Здесь будет парсинг"}