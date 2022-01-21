const toggleBtn = document.querySelector(".navbar__toggleBtn");
const menu = document.querySelector(".navbar__menu");
const logio = document.querySelector(".navbar__logio");

toggleBtn.addEventListener("click", () => {
    menu.classList.toggle("active");
    logio.classList.toggle("active");
});