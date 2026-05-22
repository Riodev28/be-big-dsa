from fastapi import APIRouter

router = APIRouter()


@router.post("/")
def analyze():
    return {
        "time_complexity": "O(n²)"
    }