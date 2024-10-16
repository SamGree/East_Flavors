const hamburger = document.getElementById("hamburger");
const navLinks = document.querySelectorAll(".nav-links");

hamburger.addEventListener("click", () => {
  navLinks.forEach((nav) => nav.classList.toggle("active"));
});