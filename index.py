from fastapi import FastAPI
from fastapi import APIRouter

from fastapi.middleware.cors import CORSMiddleware
from controllers.Methods import Bisection
from pydantic import BaseModel
from controllers.Validation import BisectionVars

import uvicorn

app = FastAPI()
router = APIRouter()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@router.get('/')
def home() :
    return {"message": "Welcome to Approximation API. Where this is just wasteland"}
@router.post('/bisection')
def bisection(vars : BisectionVars) :
    # return {"var" : "test"}
    bisection_method  = Bisection(vars)
    result = bisection_method.startIterations()
    return {"data": result}
@router.get('/tables')
def tables() :
    pass

app.include_router(router=router)

# if __name__ == "__main__" :
#     config = uvicorn.run(app, host="127.0.0.1", port=8000)