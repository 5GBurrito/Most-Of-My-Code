// Add animations to images with class photo
const photos = document.querySelectorAll('.photo');

photos.forEach(photo => {
  photo.addEventListener('mouseenter', () => {
    photo.style.transform = 'scale(1.1)';
    photo.style.transition = 'transform 0.5s ease';
  });

  photo.addEventListener('mouseleave', () => {
    photo.style.transform = 'scale(1)';
    photo.style.transition = 'transform 0.5s ease';
  });
});

// Smooth scrolling to sections
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      e.preventDefault();
  
      document.querySelector(this.getAttribute('href')).scrollIntoView({
        behavior: 'smooth'
      });
    });
  });
  