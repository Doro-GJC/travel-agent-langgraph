from fastapi import FastAPI

app = FastAPI(title="Travel Agent API")


@app.get("/")
def read_root():
    return {"message": "Travel Agent backend is running"}