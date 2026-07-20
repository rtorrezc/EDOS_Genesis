from app.schemas.onboarding import OnboardingAnalysis
def analyze_business_idea(message:str)->OnboardingAnalysis:
    text=message.lower(); model="Negocio por definir"
    if any(w in text for w in ["curso","ebook","membresía","digital"]): model="Producto digital"
    elif any(w in text for w in ["restaurante","comida","producto","tienda"]): model="Producto o servicio comercial"
    elif any(w in text for w in ["consultoría","servicio","asesoría"]): model="Servicio profesional"
    stage="Negocio en marcha" if any(w in text for w in ["ya vendo","clientes","ventas actuales"]) else "Idea"
    goal="Aumentar las ventas" if any(w in text for w in ["vender más","aumentar ventas"]) else "Validar la idea y conseguir las primeras ventas"
    customer="Personas interesadas en cultivar en casa" if "hidropon" in text else "Cliente por validar"
    project=message.strip() if len(message.strip())<=90 else message.strip()[:87].rstrip()+"..."
    confidence=min(74+(7 if model!="Negocio por definir" else 0)+(6 if customer!="Cliente por validar" else 0),92)
    return OnboardingAnalysis(project=project,business_model=model,stage=stage,probable_customer=customer,primary_goal=goal,confidence=confidence,priorities=["Definir con precisión la oferta principal","Validar el cliente y su problema prioritario","Diseñar una prueba de venta de bajo costo"])
