from fastapi import APIRouter

router = APIRouter(tags=["Countries API"])

@router.get("/country-codes")
def get_country_codes():
    return ["+63 - Philippines", "+1 - United States"]