// auth.js (mejorado)

// Base URL de la API (ajusta según el entorno de producción si es necesario)
const BASE_URL = 'http://127.0.0.1:8000/auth';

// Función para mostrar mensajes de error
function mostrarError(elemento, mensaje) {
    if (elemento) {
        elemento.innerText = mensaje;
        elemento.style.display = 'block';
    }
}

// Manejo del formulario de login
const loginForm = document.getElementById('login-form');
if (loginForm) {
    loginForm.addEventListener('submit', async (e) => {
        e.preventDefault();

        const email = document.getElementById('email-login').value;
        const password = document.getElementById('password-login').value;
        const errorElemento = document.getElementById('login-error');
        
        if (errorElemento) errorElemento.style.display = 'none'; // Ocultar mensaje de error al principio

        try {
            const response = await fetch(`${BASE_URL}/login`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ email, password })
            });

            if (!response.ok) {
                throw new Error('Credenciales incorrectas, por favor verifícalas.');
            }

            const data = await response.json();
            localStorage.setItem('token', data.token);  // Guardar el token JWT

            // Redirigir al usuario según su rol
            const userRole = data.role;
            const redirectMap = {
                cliente: 'cliente.html',
                secretaria: 'secretaria.html',
                duena: 'duena.html',
                masajista: 'masajista.html'
            };

            window.location.href = redirectMap[userRole] || 'login.html';
        } catch (error) {
            mostrarError(errorElemento, error.message);
        }
    });
}

// Manejo del formulario de registro
const registerForm = document.getElementById('register-form');
if (registerForm) {
    registerForm.addEventListener('submit', async (e) => {
        e.preventDefault();

        const name = document.getElementById('name').value;
        const email = document.getElementById('email-register').value;
        const phone = document.getElementById('phone').value;
        const password = document.getElementById('password-register').value;
        const errorElemento = document.getElementById('register-error');

        if (errorElemento) errorElemento.style.display = 'none'; // Ocultar mensaje de error al principio

        try {
            const response = await fetch(`${BASE_URL}/register`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ name, email, phone, password })
            });

            if (!response.ok) {
                throw new Error('No se pudo completar el registro. Por favor verifica los datos.');
            }

            // Registro exitoso, redirigir al login
            window.location.href = 'login.html';
        } catch (error) {
            mostrarError(errorElemento, error.message);
        }
    });
}
