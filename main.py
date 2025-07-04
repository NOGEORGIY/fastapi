app = FastAPI()

@app.get("/")
async def root():
    return {"greeting": "Hello, World!", "message": "Welcome to FastAPI!"}


@app.get("/user")
async def root():
    return {"greeting": "User", "message": "Welcome to FastAPI!"}
