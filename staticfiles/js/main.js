const hamburger = document.getElementById("hamburger");
const navLinks = document.querySelectorAll(".nav-links");

hamburger.addEventListener("click", () => {
  navLinks.forEach((nav) => nav.classList.toggle("active"));
});

const timezone = Intl.DateTimeFormat().resolvedOptions().timeZone; // e.g. "America/New_York"
document.cookie = "django_timezone=" + timezone;