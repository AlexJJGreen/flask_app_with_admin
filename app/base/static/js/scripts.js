(function () {
    let $curve = document.getElementById("curve");
    let lastKnownScrollPos = 0;
    let defaultCurveVal = 350;
    let curveRate = 3;
    let ticking = false
    let curveVal;

    function scrollEvent(scrollPos) {
        if (scrollPos >= 0 && scrollPos < defaultCurveVal) {
            curveVal = defaultCurveVal - parseFloat(scrollPos / curveRate);
            $curve.setAttribute("d", "M 800 300 Q 400 " + curveVal + " 0 300 L 0 0 L 800 0 L 300 Z");
        }
    }

    // set listener
    window.addEventListener("scroll", (e) => {
        lastKnownScrollPos = window.scrollY;

        if (!ticking) {
            window.requestAnimationFrame(() => {
                scrollEvent(lastKnownScrollPos);
                ticking = false;
            });
        }

        ticking = true;
    });
})();