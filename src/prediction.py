import os
import urllib.request
import joblib


MODEL_URL = (
    "https://github.com/JenitaDsouza01/"
    "hospital-appointment-management-system/"
    "releases/download/v1.0/no_show_model.pkl"
)

MODEL_PATH = "models/no_show_model.pkl"


def load_no_show_model(path=MODEL_PATH):
    """Load the trained no-show prediction model."""

    if not os.path.exists(path):
        os.makedirs(os.path.dirname(path), exist_ok=True)

        urllib.request.urlretrieve(
            MODEL_URL,
            path
        )

    model_data = joblib.load(path)

    model = model_data["model"]
    threshold = model_data["threshold"]

    return model, threshold


def predict_no_show(model, appointment_data):
    """Predict the probability of an appointment no-show."""

    probability = model.predict_proba(
        appointment_data
    )[0][1]

    return probability


def classify_no_show_risk(probability):
    """Classify the no-show probability into a risk level."""

    if probability < 0.30:
        return "Low Risk"
    elif probability < 0.60:
        return "Medium Risk"
    else:
        return "High Risk"