const hamburger = document.getElementById("hamburger");
const navLinks = document.querySelectorAll(".nav-links");

hamburger.addEventListener("click", () => {
  navLinks.forEach((nav) => nav.classList.toggle("active"));
});

const timezone = Intl.DateTimeFormat().resolvedOptions().timeZone; // e.g. "America/New_York"
document.cookie = "django_timezone=" + timezone;

// Add logic for active navbar link
const currentPath = window.location.pathname;

// Get all links in the navigation menu
const links = document.querySelectorAll('.nav-links a');

// Loop through links and add the 'active' class to the one that matches the current URL
links.forEach(link => {
  if (link.getAttribute('href') === currentPath) {
    link.classList.add('active');
  }
});