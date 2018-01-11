'use strict'

var slideIndex = 1;
showSlides(slideIndex);

function changeSlides(n) {
    showSlides(slideIndex += n);
}

function currentSlide(n) {
    showSlides(slideIndex = n);
}
//thumbnails

function showSlides(n) {
    var i;
    var slides = document.getElementsByClassName("slides");
    var thumb = document.getElementsByClassName("style");
    if (n > slides.length) {
        slideIndex = 1;
    }
    if (n < 1) {
        slideIndex = slides.length;
    }
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    for (i = 0; i < thumb.length; i++) {
        thumb[i].className = thumb[i].className.replace(" active", "");
    }
    slides[slideIndex - 1].style.display = "block";
    thumb[slideIndex - 1].className += " active";
}
