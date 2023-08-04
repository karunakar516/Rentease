function showSlides() {
  var slideContainers = document.getElementsByClassName("slideshow");

  for (var i = 0; i < slideContainers.length; i++) {
    var slideIndex = 0;
    var slides = slideContainers[i].getElementsByTagName("img");

    function showSlide() {
      for (var j = 0; j < slides.length; j++) {
        slides[j].style.display = "none";
      }
      slideIndex = (slideIndex + 1) % slides.length;
      slides[slideIndex].style.display = "block";
      // setTimeout(showSlide, 2000); // Change slide every 2 seconds
    }

    showSlide();
  }
}

document.addEventListener("keydown", function(event) {
  if (event.key === "ArrowLeft" || event.key === "ArrowRight") {
    plusSlides(event.key, 1);
  }
});

function plusSlides(key, n) {
  var slideContainers = document.getElementsByClassName("slideshow");

  for (var i = 0; i < slideContainers.length; i++) {
    var slides = slideContainers[i].getElementsByTagName("img");
    var currentSlideIndex = Array.from(slides).findIndex(slide => slide.style.display === "block");

    slides[currentSlideIndex].style.display = "none";

    if (key === "ArrowLeft") {
      currentSlideIndex--;
      if (currentSlideIndex < 0) {
        currentSlideIndex = slides.length - 1;
      }
    } else if (key === "ArrowRight") {
      currentSlideIndex++;
      if (currentSlideIndex >= slides.length) {
        currentSlideIndex = 0;
      }
    }

    slides[currentSlideIndex].style.display = "block";
  }
}

showSlides();
