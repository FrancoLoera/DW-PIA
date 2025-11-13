document.addEventListener("DOMContentLoaded", () => {
    const zoomInBtn = document.getElementById("zoomIn");
    const zoomOutBtn = document.getElementById("zoomOut");

    let currentZoom = 100;
    const maxZoom = 160;
    const minZoom = 70;
    const step = 10;

    function applyZoom() {
        document.documentElement.style.fontSize = `${currentZoom}%`;
        document.body.style.overflowX = "hidden";
        document.documentElement.style.overflowX = "hidden";
        document.body.style.width = "100%";
        document.documentElement.style.width = "100%";
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

    applyZoom();
});



