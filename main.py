from fastapi import FastAPI


app = FastAPI()


# get request
@app.get("/")
def hello():
    return {'message':"Hello Fast API"}