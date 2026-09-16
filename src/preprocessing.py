import pandas as pd


def prepare_appointment_data(
    gender,
    age,
    neighbourhood,
    scholarship,
    hypertension,
    diabetes,
    alcoholism,
    handcap,
    sms_received,
    waiting_days,
    appointment_weekday,
    appointment_month,
    scheduled_hour
):
    """Prepare appointment information for the no-show model."""

    data = pd.DataFrame({
        "Gender": [gender],
        "Age_Clean": [age],
        "Neighbourhood": [neighbourhood],
        "Scholarship": [scholarship],
        "Hypertension": [hypertension],
        "Diabetes": [diabetes],
        "Alcoholism": [alcoholism],
        "Handcap": [handcap],
        "SMS_received": [sms_received],
        "Waiting_Days_Clean": [waiting_days],
        "Appointment_Weekday": [appointment_weekday],
        "Appointment_Month": [appointment_month],
        "Scheduled_Hour": [scheduled_hour]
    })

    return data