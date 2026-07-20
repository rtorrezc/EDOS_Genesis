# EDOS Genesis

Primera versión funcional de EDOS, el Director Estratégico de XConecta.

## Objetivo del Sprint 1

Permitir que una persona describa lo que quiere construir, reciba una comprensión estructurada, confirme esa comprensión y obtenga tres prioridades iniciales.

## Arquitectura

- `apps/web`: interfaz conversacional en Next.js.
- `apps/api`: API en FastAPI.
- `packages/core`: reglas del Director Estratégico.
- `packages/memory`: memoria empresarial.
- `packages/strategy`: diagnóstico y roadmap.
- `docs`: decisiones y especificaciones.

## Arranque local

### API
```bash
cd apps/api
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Web
```bash
cd apps/web
npm install
npm run dev
```
