/* =========================
   POCKETPILOT AI - JS LOGIC
========================= */


/* -------------------------
   LOADING SCREEN CONTROL
   (optional extra safety)
-------------------------- */
function goToWelcome() {
    setTimeout(() => {
        window.location.href = "/welcome";
    }, 3000);
}


/* -------------------------
   COIN TOSS SOUND (optional)
-------------------------- */
function playCoinSound() {
    let audio = new Audio("/static/images/coin.mp3");
    audio.play();
}


/* -------------------------
   BUTTON CLICK ANIMATION
-------------------------- */
document.addEventListener("DOMContentLoaded", function () {

    let buttons = document.querySelectorAll("button, .btn");

    buttons.forEach(btn => {
        btn.addEventListener("click", function () {

            // small click animation
            btn.style.transform = "scale(0.95)";

            setTimeout(() => {
                btn.style.transform = "scale(1)";
            }, 150);

        });
    });

});


/* -------------------------
   RANDOM NEON BACKGROUND
   (optional dynamic effect)
-------------------------- */
function randomGradient() {

    const colors = [
        "linear-gradient(45deg,#0f172a,#1e1b4b)",
        "linear-gradient(45deg,#1a1a2e,#16213e)",
        "linear-gradient(45deg,#0f0c29,#302b63,#24243e)",
        "linear-gradient(45deg,#000428,#004e92)"
    ];

    let bg = colors[Math.floor(Math.random() * colors.length)];

    document.body.style.background = bg;
}


/* -------------------------
   AUTO RUN ON LOAD
-------------------------- */
window.onload = function () {

    randomGradient();   // random theme
    console.log("💰 PocketPilot AI Loaded Successfully");

};


/* -------------------------
   CHILD DASHBOARD - TOGGLE
   (safe check)
-------------------------- */
function toggleSpendBox() {
    let box = document.getElementById("spendBox");

    if (box) {
        if (box.style.display === "none" || box.style.display === "") {
            box.style.display = "block";
        } else {
            box.style.display = "none";
        }
    }
}
