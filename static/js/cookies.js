document.addEventListener("DOMContentLoaded", function () {

    const banner = document.getElementById("cookie-banner");
    const acceptButton = document.getElementById("cookie-accept");
    const refuseButton = document.getElementById("cookie-refuse");

    if (!banner || !acceptButton || !refuseButton) {
        return;
    }

    const consent = localStorage.getItem("analytics-consent");

    if (consent) {
        banner.style.display = "none";
    }

    acceptButton.addEventListener("click", function () {

        localStorage.setItem("analytics-consent", "accepted");

        banner.style.display = "none";
    });

    refuseButton.addEventListener("click", function () {

        localStorage.setItem("analytics-consent", "refused");

        banner.style.display = "none";
    });

});