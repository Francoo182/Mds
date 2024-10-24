import subprocess
import time
import os
import logging

logging.basicConfig(level=logging.DEBUG, filename="debug.log", filemode="w", format="%(asctime)s - %(levelname)s - %(message)s")

# Establecer el PYTHONPATH para que 'uvicorn' reconozca el paquete 'backend'
os.environ["PYTHONPATH"] = "F:\\repos\\PythonPaginaUTN\\BackendProyecto\\MDS\\backend"

# Ruta del intérprete de Python dentro del entorno virtual
python_path = "F:\\repos\\PythonPaginaUTN\\BackendProyecto\\MDS\\env\\Scripts\\python.exe"

# Ejecutar la API (con el PYTHONPATH configurado)
api_process = subprocess.Popen([python_path, "-m", "uvicorn", "main:app", "--reload"])

# Esperar unos segundos para que la API se inicie correctamente
time.sleep(2)

# Ejecutar la aplicación Tkinter (asegúrate de que la ruta es correcta)
tkinter_process = subprocess.Popen([python_path, "F:\\repos\\PythonPaginaUTN\\BackendProyecto\\MDS\\front\\login.py"])

# Esperar que ambos procesos terminen
try:
    api_process.wait()  # Espera a que el proceso de la API termine
    tkinter_process.wait()  # Espera a que el proceso de Tkinter termine
except KeyboardInterrupt:
    # Si se presiona Ctrl+C, terminamos ambos procesos
    api_process.terminate()
    tkinter_process.terminate()

