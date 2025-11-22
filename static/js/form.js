// Manejar el envío del formulario con AJAX (opcional)
document.getElementById('contactForm').addEventListener('submit', function(e) {

});

// Función para mostrar mensajes
function showMessage(type, message) {
    const messageDiv = document.createElement('div');
    messageDiv.id = 'flashMessage';
    messageDiv.className = `mt-4 p-4 ${type === 'success' ? 'bg-green-50 border-l-4 border-green-500' : 'bg-red-50 border-l-4 border-red-500'} rounded-lg`;
    
    messageDiv.innerHTML = `
        <div class="flex items-center">
            <svg class="w-6 h-6 ${type === 'success' ? 'text-green-500' : 'text-red-500'} mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                ${type === 'success' 
                    ? '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path>'
                    : '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path>'
                }
            </svg>
            <p class="${type === 'success' ? 'text-green-700' : 'text-red-700'} font-medium">${message}</p>
        </div>
    `;
    
    const form = document.getElementById('contactForm');
    form.appendChild(messageDiv);
    
    // Ocultar mensaje después de 5 segundos
    setTimeout(() => {
        messageDiv.remove();
    }, 5000);
}

// Auto-ocultar flash messages después de 5 segundos
document.addEventListener('DOMContentLoaded', function() {
    const flashMessage = document.getElementById('flashMessage');
    if (flashMessage) {
        setTimeout(() => {
            flashMessage.style.opacity = '0';
            flashMessage.style.transition = 'opacity 0.5s';
            setTimeout(() => flashMessage.remove(), 500);
        }, 5000);
    }
});