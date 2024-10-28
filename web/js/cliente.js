// cliente.js (optimizado)

// Base URL de la API (ajusta según el entorno de producción si es necesario)
const BASE_URL = 'http://127.0.0.1:8000/client'; // Cambia '127.0.0.1' según la IP o el dominio en producción

// Función para mostrar mensajes de error
function mostrarError(elemento, mensaje) {
    elemento.innerText = mensaje;
    elemento.style.display = 'block';
}

// Cargar reservas del cliente al cargar la página
document.addEventListener('DOMContentLoaded', async () => {
    const token = localStorage.getItem('token');
    const errorElemento = document.getElementById('reservas-error');
    
    errorElemento.style.display = 'none'; // Ocultar mensaje de error

    try {
        const response = await fetch(`${BASE_URL}/reservas`, {
            headers: { 'Authorization': `Bearer ${token}` }
        });

        if (!response.ok) {
            throw new Error('No se pudieron cargar las reservas.');
        }

        const reservas = await response.json();
        const tableBody = document.querySelector('#reservas-table tbody');
        tableBody.innerHTML = reservas.map(reserva => `
            <tr>
                <td>${reserva.servicio}</td>
                <td>${new Date(reserva.fecha).toLocaleDateString()}</td>
                <td>${reserva.profesional}</td>
                <td>${reserva.estado}</td>
                <td><button onclick="cancelarReserva(${reserva.id})">Cancelar</button></td>
            </tr>
        `).join('');
    } catch (error) {
        mostrarError(errorElemento, error.message);
    }
});

// Agendar una nueva cita
document.getElementById('agendar-form').addEventListener('submit', async (e) => {
    e.preventDefault();

    const servicio = document.getElementById('servicio').value;
    const fecha = document.getElementById('fecha').value;
    const profesional = document.getElementById('profesional').value;
    const errorElemento = document.getElementById('agendar-error');

    errorElemento.style.display = 'none'; // Ocultar mensaje de error

    const token = localStorage.getItem('token');
    try {
        const response = await fetch(`${BASE_URL}/agendar`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${token}`
            },
            body: JSON.stringify({ servicio, fecha, profesional })
        });

        if (!response.ok) {
            throw new Error('Error al agendar la cita. Intenta nuevamente.');
        }

        // Cita agendada exitosamente, recargar reservas
        window.location.reload();
    } catch (error) {
        mostrarError(errorElemento, error.message);
    }
});

// Realizar pago
document.getElementById('pago-form').addEventListener('submit', async (e) => {
    e.preventDefault();

    const monto = document.getElementById('monto').value;
    const metodoPago = document.getElementById('metodo-pago').value;
    const errorElemento = document.getElementById('pago-error');

    errorElemento.style.display = 'none'; // Ocultar mensaje de error

    const token = localStorage.getItem('token');
    try {
        const response = await fetch(`${BASE_URL}/pagos`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${token}`
            },
            body: JSON.stringify({ monto, metodoPago })
        });

        if (!response.ok) {
            throw new Error('Error al realizar el pago.');
        }

        // Pago realizado exitosamente
        alert('Pago realizado con éxito.');
    } catch (error) {
        mostrarError(errorElemento, error.message);
    }
});
