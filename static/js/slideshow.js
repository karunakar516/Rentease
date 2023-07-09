var slideIndex = 1;
showSlide(slideIndex);

document.addEventListener("keydown", function(event) {
  if (event.key === "ArrowLeft") {
    slideIndex--;
    if (slideIndex < 1) {
      slideIndex = 3; // Adjust the number based on the total number of slides
    }
    showSlide(slideIndex);
  } else if (event.key === "ArrowRight") {
    slideIndex++;
    if (slideIndex > 3) { // Adjust the number based on the total number of slides
      slideIndex = 1;
    }
    showSlide(slideIndex);
  }
});

function showSlide(index) {
  var slides = document.getElementsByClassName("slideshow")[0].getElementsByTagName("img");
  for (var i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  slides[index - 1].style.display = "block";
}
