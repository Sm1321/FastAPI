from fastapi import FastAPI


app = FastAPI()

# get request
@app.get("/")
def hello():
    return {'message':"Hello Fast API"}

@app.get("/1S")
def read_root():
    return {"message": "Hello, FastAPI!"}


@app.get("/about")
def about():
    return {"message": "This is From SM1321"}