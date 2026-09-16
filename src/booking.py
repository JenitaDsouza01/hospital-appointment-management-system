import pandas as pd
import os


BOOKING_COLUMNS = [
    "Appointment_ID",
    "Patient_Name",
    "Department",
    "Doctor",
    "Appointment_Date",
    "Appointment_Time",
    "No_Show_Probability",
    "Risk_Level",
    "Booking_Status"
]


def load_bookings(path="data/bookings.csv"):
    """Load existing appointment bookings."""

    if not os.path.exists(path):
        return pd.DataFrame(columns=BOOKING_COLUMNS)

    bookings = pd.read_csv(path)

    if bookings.empty:
        return pd.DataFrame(columns=BOOKING_COLUMNS)

    return bookings


def generate_appointment_id(bookings):
    """Generate a unique appointment ID."""

    if bookings.empty:
        return "APT-0001"

    return f"APT-{len(bookings) + 1:04d}"


def is_slot_booked(
    bookings,
    department,
    doctor,
    appointment_date,
    appointment_time
):
    """Check whether a particular slot is already booked."""

    if bookings.empty:
        return False

    existing_booking = bookings[
        (bookings["Department"] == department)
        & (bookings["Doctor"] == doctor)
        & (bookings["Appointment_Date"] == appointment_date)
        & (bookings["Appointment_Time"] == appointment_time)
        & (bookings["Booking_Status"] == "Booked")
    ]

    return not existing_booking.empty


def save_booking(
    bookings,
    patient_name,
    department,
    doctor,
    appointment_date,
    appointment_time,
    no_show_probability,
    risk_level,
    path="data/bookings.csv"
):
    """Save a new appointment booking."""

    appointment_id = generate_appointment_id(bookings)

    new_booking = pd.DataFrame([{
        "Appointment_ID": appointment_id,
        "Patient_Name": patient_name,
        "Department": department,
        "Doctor": doctor,
        "Appointment_Date": appointment_date,
        "Appointment_Time": appointment_time,
        "No_Show_Probability": round(
            no_show_probability * 100,
            2
        ),
        "Risk_Level": risk_level,
        "Booking_Status": "Booked"
    }])

    bookings = pd.concat(
        [bookings, new_booking],
        ignore_index=True
    )

    bookings.to_csv(
        path,
        index=False
    )

    return bookings, appointment_id