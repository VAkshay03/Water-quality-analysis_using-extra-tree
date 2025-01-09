// Get the navbar element
const navbar = document.getElementById("navbar");

// Listen for the scroll event
window.addEventListener("scroll", function() {
    if (window.scrollY > 50) {
        navbar.classList.add("scrolled"); // Add class when scrolled
    } else {
        navbar.classList.remove("scrolled"); // Remove class when at the top
    }
});
