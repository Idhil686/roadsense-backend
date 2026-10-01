"""
Basic tests for the RoadSense API.

These run against the real app, so they require accident_severity_model.pkl,
weather_encoder.pkl, sunrise_encoder.pkl, and feature_columns.pkl to be
present in the models/ folder (same as running the app normally).
"""
import pytest
from app import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_health_check(client):
    response = client.get('/health')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'ok'
    assert data['model_loaded'] is True


def test_predict_valid_payload(client):
    payload = {
        'temperature': 60,
        'humidity': 50,
        'visibility': 10,
        'wind_speed': 5,
        'precipitation': 0,
        'weather_condition': 'Clear',
        'sunrise_sunset': 'Day',
        'hour': 8,
        'day_of_week': 0,
        'junction': 0,
        'crossing': 0,
        'traffic_signal': 0,
    }
    response = client.post('/predict', json=payload)
    assert response.status_code == 200
    data = response.get_json()
    assert 'severity' in data
    assert 'severity_label' in data
    assert 'confidence' in data
    assert 'probabilities' in data


def test_predict_no_payload(client):
    response = client.post('/predict', data='', content_type='application/json')
    assert response.status_code == 400
