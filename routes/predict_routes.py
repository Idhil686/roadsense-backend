from flask import Blueprint, request, jsonify

from services.predictor import predict_severity
from utils.validators import is_valid_payload

predict_bp = Blueprint('predict', __name__)


@predict_bp.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    if not is_valid_payload(data):
        return jsonify({'error': 'No JSON payload received'}), 400

    try:
        result = predict_severity(data)
    except (KeyError, ValueError) as e:
        return jsonify({'error': f'Invalid input: {str(e)}'}), 400

    return jsonify(result)
