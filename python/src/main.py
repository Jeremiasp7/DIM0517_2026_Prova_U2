from fastapi import FastAPI

app = FastAPI()

# fluminense football club

@app.get("/hello")
def hello():
    return {"message": "Hello, World!"}


@app.get("/healthy")
def healthy():
    return {"status": "healthy"}
