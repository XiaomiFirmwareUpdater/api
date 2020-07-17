from fastapi import APIRouter

import xfu_api.database.database as db

router = APIRouter()


@router.get("/devices/all")
async def read_root():
    return [i[1] for i in db.get_devices()]


@router.get("/devices/name/{codename}")
async def get_name(codename: str):
    name = db.get_device_name(codename)
    return {codename: name}


@router.get("/devices/fullname/{codename}")
async def get_full_name(codename: str):
    name = db.get_full_name(codename)
    return {codename: name}
