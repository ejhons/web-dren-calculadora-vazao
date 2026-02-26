from fastapi import APIRouter
from schemas.flow import RationalInput, RationalOutput
from core.rational_method import rational_flow

router = APIRouter()

@router.post("/rational", response_model=RationalOutput)
def calculate_rational(data: RationalInput):
    q = rational_flow(data.C, data.intensity, data.area)
    return {"flow": q}