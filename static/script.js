document.getElementById("getLocation").addEventListener("click", function () {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(getWeatherForLocation, showError);
    } else {
        alert("Geolocation is not supported by your browser.");
    }
});

function getWeatherForLocation(position) {
    const lat = position.coords.latitude;
    const lon = position.coords.longitude;

    // Redirect the user to your Flask route with lat/lon as query parameters
    window.location.href = `/?lat=${lat}&lon=${lon}`;
}

function showError(error) {
    switch (error.code) {
        case error.PERMISSION_DENIED:
            alert("User denied the request for Geolocation.");
            break;
        case error.POSITION_UNAVAILABLE:
            alert("Location information is unavailable.");
            break;
        case error.TIMEOUT:
            alert("The request to get user location timed out.");
            break;
        case error.UNKNOWN_ERROR:
            alert("An unknown error occurred.");
            break;
    }
}
