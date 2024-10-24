from fastapi import FastAPI
from routers import clients,services,reservations,payments,reports,workers
import uvicorn


app = FastAPI()

app.include_router(clients.router)
app.include_router(services.router)
app.include_router(reservations.router)
app.include_router(payments.router)
app.include_router(reports.router) 
app.include_router(workers.router)
@app.get("/")
def read_root():
    return {"message": "Bienvenido al SPA 'Sentirse Bien' API"}