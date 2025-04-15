// main.js

// Example: Toggle nav or mobile menu (if used)
document.addEventListener('DOMContentLoaded', () => {
  const toggleMenuBtn = document.querySelector('#toggleMenu');
  const navMenu = document.querySelector('#navMenu');

  if (toggleMenuBtn && navMenu) {
    toggleMenuBtn.addEventListener('click', () => {
      navMenu.classList.toggle('hidden');
    });
  }

  // Example: Alert on successful signup/login (can be improved with proper backend messages)
  const flashMessage = document.querySelector('#flash-message');
  if (flashMessage) {
    setTimeout(() => {
      flashMessage.style.display = 'none';
    }, 3000); // auto-hide after 3 seconds
  }
});
