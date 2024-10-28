from fastapi import APIRouter, HTTPException
from crud import *
from models import Reserva
from fastapi.concurrency import run_in_threadpool

router = APIRouter()

@router.post("/reservas")
async def crear_reserva(reserva: Reserva):
    resultado = create_reserva(reserva)
    
    if "error" in resultado:
        raise HTTPException(status_code=400, detail=resultado["error"])
    
    return resultado
@router.get("/reservas/total")
async def obtener_todas_las_reservas():
    reservas = await run_in_threadpool(get_todas_las_reservas)  # Sin paréntesis, pasamos la función como referencia
    return reservas
    # print("la loquita")
    # reservas = await run_in_threadpool(get_todas_las_reservas)

@router.get("/reservas/dia")
async def obtener_reservas_del_dia():
    reservas = await run_in_threadpool(get_reservas_del_dia)
    if "error" in reservas:
        raise HTTPException(status_code=400, detail=reservas["error"])
    return reservas
@router.get("/reservas/{cliente_id}")
async def obtener_reservas_by_cliente(cliente_id: int):
    reservasxCliente = get_reservas_by_cliente(cliente_id)
    if "error" in reservasxCliente:
        raise HTTPException(status_code=400, detail=reservasxCliente["error"])
    return reservasxCliente
@router.get("/reservasf/{fecha}")
async def obtener_reservas_dela_fecha(fecha: str):
    # Pasa la función y el argumento como parámetros de run_in_threadpool
    reservas = await run_in_threadpool(get_reservas_por_fecha, fecha)
    if "error" in reservas:
        raise HTTPException(status_code=400, detail=reservas["error"])
    return reservas