import os
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from routers import clients,services,reservations,payments,reports,workers



app = FastAPI()

app.include_router(clients.router)
app.include_router(services.router)
app.include_router(reservations.router)
app.include_router(payments.router)
app.include_router(reports.router) 
app.include_router(workers.router)

# Sirviendo archivos estáticos desde "web"
app.mount("/static", StaticFiles(directory=os.path.join(os.path.dirname(__file__), "../web")), name="static")

# Directorio de plantillas (HTML dinámico)
templates = Jinja2Templates(directory="web")

@app.get("/")
async def read_index(request: Request):
    # Puedes pasar datos dinámicos al template
    return templates.TemplateResponse("index3.html", {"request": request, "message": "Bienvenido a Spa Sentirse Bien"})