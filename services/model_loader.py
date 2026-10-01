import joblib

from config import (
    MODEL_PATH,
    WEATHER_ENCODER_PATH,
    SUNRISE_ENCODER_PATH,
    FEATURE_COLUMNS_PATH,
)

# These are loaded ONCE when the app starts, not on every request.
# Every other file that needs the model or encoders imports them from here.
model = joblib.load(MODEL_PATH)
weather_encoder = joblib.load(WEATHER_ENCODER_PATH)
sunrise_encoder = joblib.load(SUNRISE_ENCODER_PATH)
feature_columns = joblib.load(FEATURE_COLUMNS_PATH)
