(
    () => {
        let menuIcon = document.getElementById("menuIcon");
        let menu = document.getElementById("menu");

        menuIcon.addEventListener("click", () => {
            if (menu.classList.contains("expanded")) {
                menu.classList.remove("expanded");
                menuIcon.firstChild.classList = "fa-solid fa-bars";
            } else {
                menu.classList.add("expanded");
                menuIcon.firstChild.classList = "fa-solid fa-minus";
            }
        });

    })();