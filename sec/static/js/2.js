
    // Get the sliding text element
const slidingText = document.querySelector('.sliding-text');

// Calculate the width of the slider
const sliderWidth = document.querySelector('.slider').offsetWidth;

// Function to animate the text
function animateText() {
  let position = sliderWidth;
  const animationDuration = 150; // Duration of animation in milliseconds

  function frame() {
    if (position <= -slidingText.offsetWidth) {
      position = sliderWidth; // Reset position when text goes out of view
    } else {
      position -= 0.5; // Move text 1 pixel to the left
      slidingText.style.left = position + 'px';
    }
    requestAnimationFrame(frame);
  }

  // Start the animation
  frame();
}

// Call the animateText function to start the animation
animateText();


