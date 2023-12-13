document.addEventListener("DOMContentLoaded", function () {
  // Check if the initial time is stored in local storage
  let startTime = localStorage.getItem("countdownStart");

  if (!startTime) {
    // Set initial time to 2 days from now
    const twoDaysInSeconds = 2 * 24 * 60 * 60;
    startTime = Math.floor(Date.now() / 1000) + twoDaysInSeconds;

    // Store the initial time in local storage
    localStorage.setItem("countdownStart", startTime);
  }

  // Call the function to start the countdown
  startCountdown(startTime);
});

function startCountdown(startTime) {
  const countdownElement = document.getElementById("countdown");

  function updateCountdown() {
    const currentTime = Math.floor(Date.now() / 1000);
    const timeRemaining = startTime - currentTime;

    if (timeRemaining <= 0) {
      countdownElement.innerHTML = "Under Construction!";
    } else {
      const days = Math.floor(timeRemaining / (24 * 60 * 60));
      const hours = Math.floor((timeRemaining % (24 * 60 * 60)) / (60 * 60));
      const minutes = Math.floor((timeRemaining % (60 * 60)) / 60);
      const seconds = timeRemaining % 60;

      countdownElement.innerHTML = `${days}d ${hours}h ${minutes}m ${seconds}s`;
    }
  }

  // Call the updateCountdown function every second
  setInterval(updateCountdown, 1000);

  // Initial call to set the countdown immediately
  updateCountdown();
}
