document.addEventListener("DOMContentLoaded", () => {
    const toggleBtn = document.getElementById("darkModeToggle");
    const html = document.documentElement; // cambia en <html>, no en <body>

    if (!toggleBtn) return;

    // Aplica tema guardado
    const currentTheme = localStorage.getItem("theme");
    if (currentTheme === "dark") {
        html.setAttribute("data-theme", "dark");
        toggleBtn.innerHTML = '<i class="bi bi-brightness-high-fill"></i>';
    }

    toggleBtn.addEventListener("click", () => {
        const isDark = html.getAttribute("data-theme") === "dark";
        if (isDark) {
        html.removeAttribute("data-theme");
        toggleBtn.innerHTML = '<i class="bi bi-moon-fill"></i>';
        localStorage.setItem("theme", "light");
        } else {
        html.setAttribute("data-theme", "dark");
        toggleBtn.innerHTML = '<i class="bi bi-brightness-high-fill"></i>';
        localStorage.setItem("theme", "dark");
        }
    });
});
