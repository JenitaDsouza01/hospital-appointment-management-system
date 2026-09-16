import pandas as pd


def load_slot_data(path="../data/available_slots.csv"):
    """Load available appointment slots."""
    return pd.read_csv(path)


def load_hospital_config(path="../data/hospital_config.csv"):
    """Load hospital capacity configuration."""
    return pd.read_csv(path)


def classify_capacity(utilization):
    """Classify capacity utilization."""
    if utilization < 70:
        return "Low"
    elif utilization < 90:
        return "Normal"
    elif utilization <= 100:
        return "High"
    else:
        return "Over Capacity"


def capacity_recommendation(spare_capacity, utilization):
    """Generate a capacity recommendation."""
    if spare_capacity < 0:
        return "Consider additional slots or capacity reallocation"
    elif spare_capacity == 0:
        return "Capacity fully utilized"
    elif utilization >= 85:
        return "Monitor capacity closely"
    else:
        return "Capacity available"


def recommend_slots(
    available_slots,
    department,
    preferred_time="09:00 AM",
    number_of_slots=5
):
    """Recommend appointment slots closest to the preferred time."""

    department_slots = available_slots[
        available_slots["Department"] == department
    ].copy()

    if department_slots.empty:
        return pd.DataFrame()

    preferred = pd.to_datetime(
        preferred_time,
        format="%I:%M %p"
    )

    department_slots["Appointment_Time_dt"] = pd.to_datetime(
        department_slots["Appointment_Time"],
        format="%I:%M %p"
    )

    department_slots["Time_Difference_Minutes"] = (
        department_slots["Appointment_Time_dt"] - preferred
    ).abs().dt.total_seconds() / 60

    department_slots = department_slots.sort_values(
        "Time_Difference_Minutes"
    )

    department_slots["Recommendation_Rank"] = range(
        1,
        len(department_slots) + 1
    )

    return department_slots.head(number_of_slots)[
        [
            "Recommendation_Rank",
            "Department",
            "Doctor",
            "Slot_Number",
            "Appointment_Time",
            "Time_Difference_Minutes"
        ]
    ]