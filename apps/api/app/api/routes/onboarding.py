from fastapi import APIRouter
from app.core.understanding import analyze_business_idea
from app.schemas.onboarding import OnboardingAnalysis,OnboardingRequest
router=APIRouter(prefix="/onboarding",tags=["onboarding"])
@router.post("/analyze",response_model=OnboardingAnalysis)
def analyze_onboarding(payload:OnboardingRequest)->OnboardingAnalysis: return analyze_business_idea(payload.message)
