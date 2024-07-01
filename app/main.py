from fastapi import FastAPI
from typing import Union
from pydantic import BaseModel

tags_metadata = [
    {
        "name": "Integration Api - Transactions",
        "description": "Integration Api - Transactions",
    },
    {
        "name": "Integration Api - Services",
        "description": "Integration Api - Services",
    },
    {
        "name": "Configuration Api",
        "description": "Configuration Api",
    },
    {
        "name": "Auth",
        "description": "Auth",
    },
]

app = FastAPI(openapi_tags=tags_metadata)

class EService(BaseModel):
    id: float
    extId: str
    name: str
    image: Union[str, None] = None
    meta: Union[str, None] = None

class Config(BaseModel):
    type: float
    url: str

class AuthRequest(BaseModel):
    clientId: str
    clientSecret: str


@app.post("/eservice/transaction/{extId}", tags=["Integration Api - Transactions"])
async def initializeTransaction(extId: str):
    return {"message": "Hello World"}

@app.delete("/eservice/transaction/{extId}/{extTransactionId}", tags=["Integration Api - Transactions"])
async def deleteTransaction(extId: str, extTransactionId: str):
    return {"message": "Hello World"}

@app.get("/eservices/{jopp-jib}", tags=["Integration Api - Services"])
async def getTransactionByJib(joppJib: str)->EService:
    return EService;


@app.put("/eservice/webhook/config", tags=["Configuration Api"])
async def updateConfig(config: Config)->Config:
    return {"message": "Hello World"}

@app.post("/eservice/auth", tags=["Auth"])
async def authorize(authRequest: AuthRequest):
    return {"message": "Hello World"}