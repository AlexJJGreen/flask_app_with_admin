(
    () => {
        let menuIcon = document.getElementById("menuIcon");
        let menu = document.getElementById("menu");

        menuIcon.addEventListener("click", () => {
            if (menu.classList.contains("expanded")) {
                menu.classList.remove("expanded");
            } else {
                menu.classList.add("expanded");
            }
        });

    })();