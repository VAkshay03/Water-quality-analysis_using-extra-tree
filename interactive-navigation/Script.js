// Get the navbar element
const navbar = document.getElementById("navbar");

// Listen for the scroll event
window.addEventListener("scroll", function() {
    // Add 'scrolled' class when scrolling down 50px or more
    if (window.scrollY > 50) {
        navbar.classList.add("scrolled");
    } else {
        navbar.classList.remove("scrolled");
    }
});
