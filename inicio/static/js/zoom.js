document.addEventListener("DOMContentLoaded", () => {
    const zoomInBtn = document.getElementById("zoomIn");
    const zoomOutBtn = document.getElementById("zoomOut");

    // Tamaño base de fuente (usaremos esto para escalar todo el sitio)
    let currentZoom = 100; // %
    const maxZoom = 130;
    const minZoom = 80;
    const step = 10;

    // Aplica el zoom ajustando la raíz del documento (html)
    function applyZoom() {
        document.documentElement.style.fontSize = `${currentZoom}%`;
    }

    zoomInBtn.addEventListener("click", () => {
        if (currentZoom < maxZoom) {
            currentZoom += step;
            applyZoom();
        }
    });

    zoomOutBtn.addEventListener("click", () => {
        if (currentZoom > minZoom) {
            currentZoom -= step;
            applyZoom();
        }
    });
});
