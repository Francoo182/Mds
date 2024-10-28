from fastapi import APIRouter
from crud import *
from models import *
import uvicorn

router = APIRouter()
class Requests:
    @router.post("/clients/", response_model=dict)
    def create_client(cliente: Cliente):
        return create_client(cliente)
    @router.get("/clientsg/")
    def get_clients():
        return get_clients()
    @router.get("/clients/{cliente_id}")
    def get_client():
        return get_cliente_by_id(cliente_id=int)
    @router.get("/clients/xday_and_services")
    def get_clients_xday_and_services():
        return get_clients_xday_and_services()

    @router.get("/clients/xprofesional_byHours")
    def get_clients_xprofesional_byHours():
        return get_clients_xprofesional_byHours()

    @router.get("/clients/login/{email}/{password}")
    def authenticate_client(email:str,password:str):
        return authenticate_client(email,password)
    
    @router.get("/clients/email/{email}")
    def clienteXMail(email:str):
        return get_cliente_by_email(email)