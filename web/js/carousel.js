// carousel.js

let currentSlide = 0;
const slides = document.querySelectorAll('.slide');
const totalSlides = slides.length;
const prev = document.querySelector('.prev');
const next = document.querySelector('.next');

// Mostrar la diapositiva actual
function showSlide(slideIndex) {
    slides.forEach((slide, index) => {
        slide.classList.remove('active');
        if (index === slideIndex) {
            slide.classList.add('active');
        }
    });
}

// Cambiar a la siguiente diapositiva
function nextSlide() {
    currentSlide = (currentSlide + 1) % totalSlides;
    showSlide(currentSlide);
}

// Cambiar a la diapositiva anterior
function prevSlide() {
    currentSlide = (currentSlide - 1 + totalSlides) % totalSlides;
    showSlide(currentSlide);
}

// Inicializar el carrusel solo si hay diapositivas
if (slides.length > 0) {
    showSlide(currentSlide); // Mostrar la primera diapositiva

    // Cambiar de imagen automáticamente cada 5 segundos
    const autoSlideInterval = setInterval(nextSlide, 5000);

    // Event listeners para los botones de navegación
    if (next && prev) {
        next.addEventListener('click', () => {
            clearInterval(autoSlideInterval); // Pausar auto-slide al hacer clic
            nextSlide();
        });

        prev.addEventListener('click', () => {
            clearInterval(autoSlideInterval); // Pausar auto-slide al hacer clic
            prevSlide();
        });
    }
}
