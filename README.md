# RoadSense — Backend

Flask API that predicts US traffic accident severity (1–4) from scene conditions,
using a Random Forest model trained with SMOTE (for class imbalance) and
GridSearchCV (for hyperparameter tuning).

## Project Structure

```
roadsense-backend/
├── app.py                  # Entry point — creates the Flask app and registers routes
├── config.py                # Paths to model files + severity label mapping
├── requirements.txt
├── README.md
│
├── models/                  # Trained model + supporting encoders
│   ├── accident_severity_model.pkl
│   ├── feature_columns.pkl
│   ├── sunrise_encoder.pkl
│   └── weather_encoder.pkl
│
├── services/                 # Business logic (ML side)
│   ├── model_loader.py        # Loads model + encoders once at startup
│   └── predictor.py            # Builds feature vectors and runs predictions
│
├── routes/                   # Web layer (Flask blueprints)
│   ├── main_routes.py          # '/' homepage and '/health' check
│   └── predict_routes.py       # '/predict' endpoint
│
├── utils/
│   └── validators.py           # Basic payload validation
│
├── templates/
│   └── index.html              # Frontend UI
│
└── tests/
    └── test_predict.py         # Unit tests for the API
```

## Setup

```bash
pip install -r requirements.txt
python app.py
```

The app runs at `http://localhost:5000`.

## API Endpoints

### `GET /`
Serves the frontend UI.

### `GET /health`
Returns API and model status.
```json
{ "status": "ok", "model_loaded": true }
```

### `POST /predict`
Accepts scene conditions as JSON and returns the predicted severity.

**Request body:**
```json
{
  "temperature": 60,
  "humidity": 50,
  "visibility": 10,
  "wind_speed": 5,
  "precipitation": 0,
  "weather_condition": "Clear",
  "sunrise_sunset": "Day",
  "hour": 8,
  "day_of_week": 0,
  "junction": 0,
  "crossing": 0,
  "traffic_signal": 0
}
```

**Response:**
```json
{
  "severity": 2,
  "severity_label": "Moderate - noticeable delay",
  "confidence": 0.82,
  "probabilities": { "1": 0.02, "2": 0.82, "3": 0.14, "4": 0.02 }
}
```

## Running Tests

```bash
pytest tests/
```
## Model file

accident_severity_model.pkl is too large for GitHub (about 667 MB), so it is not in this repo.
Download it from the link below and put it in the models folder:

https://drive.google.com/file/d/1BBkAojTb6mO2D0MOTvd3XwopkIPsceQ2/view?usp=sharing
