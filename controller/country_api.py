from fastapi import APIRouter

router = APIRouter(tags=["Countries API"])

@router.get("/countries")
def get_country_codes():
    return ["+63 - Phil"]