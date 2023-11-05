let slideIndex = 1;
  showSlides(slideIndex);

  // Function to move to the next slide
  function nextSlide() {
    plusSlides(1);
  }

  // Auto move the slider every 5 seconds
  let slideInterval = setInterval(nextSlide, 5000);

  // Pause the auto slide when navigating manually
  const prevButton = document.querySelector(".prev");
  const nextButton = document.querySelector(".next");

  prevButton.addEventListener("click", function() {
    clearInterval(slideInterval); // Pause auto slide
    slideInterval = setInterval(nextSlide, 5000); // Resume auto slide
  });

  nextButton.addEventListener("click", function() {
    clearInterval(slideInterval); // Pause auto slide
    slideInterval = setInterval(nextSlide, 5000); // Resume auto slide
  });


// Manual navigation by clicking dots
const dots = document.getElementsByClassName("dot");
for (let i = 0; i < dots.length; i++) {
  dots[i].addEventListener("click", function () {
    currentSlide(i + 1);
  });
}

function plusSlides(n) {
  showSlides(slideIndex += n);
}

function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  let i;
  let slides = document.getElementsByClassName("mySlides");
  let dots = document.getElementsByClassName("dot");
  if (n > slides.length) { slideIndex = 1 }
  if (n < 1) { slideIndex = slides.length }
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex - 1].style.display = "block";
  dots[slideIndex - 1].className += " active";
}
