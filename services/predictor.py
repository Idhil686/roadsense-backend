import numpy as np

from config import SEVERITY_LABELS
from services.model_loader import model, weather_encoder, sunrise_encoder, feature_columns


def build_feature_vector(payload):
    """Turn a raw JSON payload from the frontend into the numeric array
    the model expects, in the exact column order it was trained on."""
    weather_condition = payload.get('weather_condition', 'Clear')
    sunrise_sunset = payload.get('sunrise_sunset', 'Day')

    try:
        weather_enc = int(weather_encoder.transform([weather_condition])[0])
    except ValueError:
        weather_enc = int(weather_encoder.transform(['Other'])[0])

    try:
        sunrise_enc = int(sunrise_encoder.transform([sunrise_sunset])[0])
    except ValueError:
        sunrise_enc = int(sunrise_encoder.transform(['Day'])[0])

    row = {
        'Temperature(F)': float(payload.get('temperature', 60)),
        'Humidity(%)': float(payload.get('humidity', 50)),
        'Visibility(mi)': float(payload.get('visibility', 10)),
        'Wind_Speed(mph)': float(payload.get('wind_speed', 5)),
        'Precipitation(in)': float(payload.get('precipitation', 0)),
        'Hour': int(payload.get('hour', 12)),
        'DayOfWeek': int(payload.get('day_of_week', 0)),
        'Weather_Enc': weather_enc,
        'Sunrise_Enc': sunrise_enc,
        'Junction': int(payload.get('junction', 0)),
        'Crossing': int(payload.get('crossing', 0)),
        'Traffic_Signal': int(payload.get('traffic_signal', 0)),
    }

    return np.array([[row[col] for col in feature_columns]])


def predict_severity(payload):
    """Run the full prediction pipeline on a raw payload and return
    a JSON-ready dict with severity, label, confidence, and probabilities."""
    features = build_feature_vector(payload)

    prediction = int(model.predict(features)[0])
    probabilities = model.predict_proba(features)[0]
    classes = model.classes_

    confidence = float(max(probabilities))
    prob_breakdown = {
        int(cls): round(float(prob), 4)
        for cls, prob in zip(classes, probabilities)
    }

    return {
        'severity': prediction,
        'severity_label': SEVERITY_LABELS.get(prediction, 'Unknown'),
        'confidence': round(confidence, 4),
        'probabilities': prob_breakdown
    }
