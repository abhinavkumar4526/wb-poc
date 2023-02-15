from fastapi import FastAPI, APIRouter, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def index():
    return {"title": "Hello :)"}


@app.get("/demo/api1")
async def get_list_of_factors():
    data = "Hello this is a sample api"
    return {"data": {"name":"John", "age":30, "nominees":["Jacob", "Jerry"], "account_type": "current","is_card_issued": True}, "details": {}}