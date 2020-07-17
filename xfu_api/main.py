from argparse import ArgumentParser

import uvicorn
from fastapi import FastAPI

from xfu_api.database import SessionLocal
from xfu_api.routers import devices


def get_db():
    db = None
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


api = FastAPI()
api.include_router(devices.router)

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-d", "--development", help="Run in development mode", action="store_true")
    args = parser.parse_args()
    if args.development:
        uvicorn.run("main:api", host="127.0.0.1", port=8081, reload=True)
    else:
        uvicorn.run(api, host="127.0.0.1", port=8081)
