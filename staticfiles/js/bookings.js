// Select all cancel booking buttons and add event listeners to handle the cancellation.
const cancelBookingBtns = document.querySelectorAll(".cancel-booking");
cancelBookingBtns.forEach((booking) => booking.addEventListener("click", cancelBooking));

/*
  Handles the booking cancellation when a user clicks the cancel button.
  Fetches the booking ID from the data attribute.
  Sends a PATCH request to cancel the booking using the CSRF token for security.
  Removes the booking element from the DOM if the cancellation is successful.
  Logs an error message if the cancellation fails.
 */
async function cancelBooking(e) {
  const bookingElement = e.target.closest(".booking");
  const bookingId = bookingElement.dataset.bookingid;
  const token = Cookies.get("csrftoken");

  const hostLocation = window.location.origin;

  /* Send the PATCH request to cancel the booking*/
  const response = await fetch(`${hostLocation}/booking/cancel-booking/${bookingId}/`, {
    method: "PATCH",
    credentials: "same-origin",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": token,
    },
  });
  /* If successful, remove the booking element from the DOM*/
  if (response.ok) {
    bookingElement.remove();
    console.log("Booking canceled successfully!");
  } else if (!response.ok) {
    const errorData = await response.json();
    console.error("Error:", errorData);
    throw new Error("Error happened while canceling booking");
  }
}