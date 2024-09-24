window.document$  = document$          /* Document observable */ 

document$.subscribe(function() {

  const projects = document.querySelectorAll(".button");
  const projectsBlock = document.querySelectorAll(".project-block");
  const projectsDescription = document.querySelectorAll(".project-description");
  const projectsDescriptionContainer = document.querySelectorAll(".project-description-container");
  const close = document.querySelectorAll(".close-project");

  for (let a = 0; a < projects.length; a++){
    projects[a].onclick = function() {
        projectsDescription[a].style.display = "flex";
        projectsDescriptionContainer[a].style.display = "flex";
        for (let b = 0; b < projects.length; b++){
            close[b].onclick = function() {
            projectsDescription[b].style.display = "none";
            projectsDescriptionContainer[b].style.display = "none";
            }
            projectsDescriptionContainer[b].onclick = function() {
            projectsDescription[b].style.display = "none";
            projectsDescriptionContainer[b].style.display = "none";
            }
        }
    }

    projectsBlock[a].onclick = function() {
        projectsDescription[a].style.display = "flex";
        projectsDescriptionContainer[a].style.display = "flex";
        for (let b = 0; b < projects.length; b++){
            close[b].onclick = function() {
            projectsDescription[b].style.display = "none";
            projectsDescriptionContainer[b].style.display = "none";
            }
            projectsDescriptionContainer[b].onclick = function() {
            projectsDescription[b].style.display = "none";
            projectsDescriptionContainer[b].style.display = "none";
            }
        }
    }
  }

  const popupOverlay = document.querySelector(".popup-overlay");
  const popup = document.querySelector(".video-popup iframe");
  const videoButton = document.querySelectorAll(".video-button");

  videoButton.forEach((link) => {
      link.addEventListener("click", () => {
      popupOverlay.classList.add("active");
      let videoLink = `https://www.youtube.com/embed/${link.dataset.link}?controls=0&rel=0`;
      popup.src = videoLink;
      document.querySelector(".ytp-expand-pause-overlay .ytp-pause-overlay").style.display="none";
      });
  });

  popupOverlay.addEventListener("click", () => {
      popupOverlay.classList.remove("active");
      let videoLink = `https://www.youtube.com/embed/`;
      popup.src = videoLink;
  });

  var slideIndex = 1;
  function showSlides() {
      let i;
      let slides = document.getElementsByClassName("carousel-block");
      let descriptionSlide = document.getElementsByClassName("carousel-text");
      let numberSlide = document.getElementsByClassName("carousel-number");
      for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";
      descriptionSlide[i].style.display = "none";
      numberSlide[i].style.display = "none";
      }
      slideIndex++;
      if (slideIndex > slides.length) {slideIndex = 1}
      slides[slideIndex-1].style.display = "block";
      descriptionSlide[slideIndex-1].style.display = "block";
      numberSlide[slideIndex-1].style.display = "block";
  }

    setInterval(function () {
        try {
        showSlides();
        } catch (e) {
        }
    }, 6000);
})