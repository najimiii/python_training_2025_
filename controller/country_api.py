from fastapi import APIRouter
from domain.service_response import ServiceResponse

router = APIRouter(tags=["Countries API"])

@router.get("/country-codes")
def get_country_codes()->ServiceResponse[list[str]]:
    return ["+63 - Philippines", "+1 - United States"]