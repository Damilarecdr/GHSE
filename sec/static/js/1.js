
  // Toggle menu function for mobile
  function toggleMenu() {
    var menu = document.getElementById('main-menu');
    menu.style.display = menu.style.display === 'flex' ? 'none' : 'flex';
  }

  // Simple slider functionality with fade effect
  let slideIndex = 0;
  const slides = document.querySelectorAll('#slider > div');
  
  function showSlides() {
    slides.forEach((slide, index) => {
      slide.querySelector('img').classList.remove('active');
      slide.style.display = 'none';
    });
    slideIndex++;
    if (slideIndex > slides.length) {
      slideIndex = 1;
    }
    slides[slideIndex - 1].style.display = 'block';
    setTimeout(() => {
      slides[slideIndex - 1].querySelector('img').classList.add('active');
    }, 10); // Ensure the transition effect applies
    setTimeout(showSlides, 3000); // Change image every 3 seconds
  }

  showSlides();
