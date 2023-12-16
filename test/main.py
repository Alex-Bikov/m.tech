from datetime import date
from enum import Enum
from typing import Optional, List

from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl

app = FastAPI(title="Hello M.tech")


@app.get("/")
async def read_root():
    return {"Hello": "World"}

test = [
    {"id": 1, "create": "2023-12-14",
        "log": {
            "ip": "172.16.31.10",
            "method": "POST",
            "uri": "http://127.0.0",
            "status_code": 200
        }
    },
    {"id": 2, "create": "2023-12-13",
        "log": {
         "ip": "162.10.21.15",
         "method": "POST",
         "uri": "http://127.1.1",
         "status_code": 200
        }
    },
    {"id": 3, "create": "2023-12-12",
        "log": {
            "ip": "170.36.61.11",
            "method": "GET",
            "uri": "http://127.15.15",
            "status_code": 200
        }
    }
]

class HttpMethod(str, Enum):
    GET = 'GET'
    POST = 'POST'
    DELETE = 'DELETE'
    PUT = 'PUT'



class Log(BaseModel):
    ip: str
    method: HttpMethod
    uri: HttpUrl
    status_code: int

class Item(BaseModel):
    id: int
    create: date
    log: Log

@app.get("/api/data{user_id}")
def read_api_data(user_id: int):
    return [user for user in test if user.get("id") == user_id]

@app.get("/post")
def get_post(user_id: int):
    query = f"SELECT * FROM users WHERE id = {user_id}"



@app.post("/api/data")
def post_api_data(item: list[Item]):
    test.extend(item)
    return {"status": 200, "data": test}
