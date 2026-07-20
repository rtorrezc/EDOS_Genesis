from fastapi.testclient import TestClient
from app.main import app
client=TestClient(app)
def test_health(): assert client.get("/health").json()=={"status":"ok"}
def test_analyze_hydroponics_course():
    r=client.post("/v1/onboarding/analyze",json={"message":"Quiero vender un curso de hidroponía"})
    assert r.status_code==200
    data=r.json(); assert data["business_model"]=="Producto digital"; assert data["confidence"]>=80; assert len(data["priorities"])==3
