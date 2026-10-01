def is_valid_payload(data):
    """Basic sanity check that the incoming JSON is a non-empty dict.
    Deeper field-level validation still happens in predictor.py, since
    that's where we know exactly what each field should look like."""
    return isinstance(data, dict) and len(data) > 0
