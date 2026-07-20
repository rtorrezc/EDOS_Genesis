from pydantic import BaseModel,Field
class OnboardingRequest(BaseModel): message:str=Field(min_length=10,max_length=4000)
class OnboardingAnalysis(BaseModel):
    project:str
    business_model:str
    stage:str
    probable_customer:str
    primary_goal:str
    confidence:int=Field(ge=0,le=100)
    priorities:list[str]
