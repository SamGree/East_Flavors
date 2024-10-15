const cancelBookingBtns = document.querySelectorAll(".cancel-booking");
cancelBookingBtns.forEach((booking) => booking.addEventListener("click", cancelBooking));

async function cancelBooking(e) {
  const bookingElement = e.target.closest(".booking");
  const bookingId = bookingElement.dataset.bookingid;
  const token = Cookies.get("csrftoken");

  const hostLocation = window.location.origin;

  const response = await fetch(`${hostLocation}/booking/cancel-booking/${bookingId}/`, {
    method: "PATCH",
    credentials: "same-origin",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": token,
    },
  });

  if (response.ok) {
    bookingElement.remove();
    console.log("Booking canceled successfully!");
  } else if (!response.ok) {
    const errorData = await response.json();
    console.error("Error:", errorData);
    throw new Error("Error happened while canceling booking");
  }
}
