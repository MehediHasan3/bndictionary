const header = document.getElementById('header');

header.addEventListener('click', () => {
  window.location.href = 'http://127.0.0.1:8000';
});

header.style.textAlign = 'center';
header.style.cursor = 'pointer';
