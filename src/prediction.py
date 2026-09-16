import joblib


def load_no_show_model(path="../models/no_show_model.pkl"):
    """Load the trained no-show prediction model."""
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