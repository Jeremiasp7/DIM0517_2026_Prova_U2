from fastapi import FastAPI

app = FastAPI()

# fluminense football club

# mais um teste, só pra garantir né

# último, prometo

@app.get("/hello")
def hello():
    return {"message": "Hello, World!"}


@app.get("/healthy")
def healthy():
    return {"status": "healthy"}
