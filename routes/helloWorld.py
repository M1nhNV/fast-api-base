from fastapi import APIRouter

router = APIRouter(
    prefix="/hello-world"
)


@router.get("")
def read_root():
    return {"Hello": "World"}
