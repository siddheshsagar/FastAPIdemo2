from fastapi import FastAPI
from typing import Optional
# we use pydantic module to post a request to API. We create class which refer to a pydentic model.
from pydantic import BaseModel  # for declaring & defining the post requests 


app = FastAPI() # FastAPI instance


@app.get("/")
def index():
    return {"data":{"name":"Siddhesh"}}

@app.get("/about")
def about(id,limit,published=True):
    return f"db{id} limit is {limit} and it is {published}"


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]


@app.post("/blog")
def create_blog(request:Blog):
    return {"data":f"blog is created using with {request.title}"}