from fastapi import FastAPI
import uvicorn


app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Welcome to my FastAPI app!"}

@app.get("/about/{id}")
def read_root(id:int):
    return {"message": id}

@app.get("/about")
def read_root(limit, published:bool):
    if published:
        return {"message":published}
    else:
        return {"message": limit}
    
if __name__ == '_main_':
    uvicorn.run(app,host="127.0.0.1", port=8080)