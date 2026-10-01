import os

# Base directory of the project (where this config.py lives)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Folder where the trained model + encoders live
MODEL_DIR = os.path.join(BASE_DIR, 'models')

# Individual file paths for the model and its supporting objects
MODEL_PATH = os.path.join(MODEL_DIR, 'accident_severity_model.pkl')
WEATHER_ENCODER_PATH = os.path.join(MODEL_DIR, 'weather_encoder.pkl')
SUNRISE_ENCODER_PATH = os.path.join(MODEL_DIR, 'sunrise_encoder.pkl')
FEATURE_COLUMNS_PATH = os.path.join(MODEL_DIR, 'feature_columns.pkl')

# Human-readable labels for each predicted severity class
SEVERITY_LABELS = {
    1: 'Minor - short delay expected',
    2: 'Moderate - noticeable delay',
    3: 'Serious - significant delay/impact',
    4: 'Severe - major delay, high impact'
}
