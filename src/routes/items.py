from fastapi import APIRouter

router = APIRouter()


@router.get("/route/banana")
async def banana():
    return {"username": "minion"}


@router.get("/route/apple")
async def apple():
    return {"username": "monkey"}


@router.get("/route/chicken")
async def chicken():
    return {"username": "rooster"}


@router.get("/route/bird")
async def bird():
    return {"username": "eagle"}

